from django.conf import settings
from .serializers import MothershipSerializer,ShipSerializer,CrewSerializer
from django.db import transaction
from .models import Mothership,Ship,Crew
import random, string
from rest_framework import status
import names 

def mothership_get(id=None):
        
    try:
        if id == None:    
            mList = Mothership.objects.all()
            serializer = MothershipSerializer(mList,many=True)
        else:            
            mList = Mothership.objects.get(pk=id)
            serializer = MothershipSerializer(mList,many=False)

        return status.HTTP_200_OK , serializer.data
           

    except Mothership.DoesNotExist:           
        return status.HTTP_400_BAD_REQUEST , {"error":"Mothership " + str(id) + " does not Exist"}
    
@transaction.atomic
def mothership_create(name,capacity):
    try:
        item = {"name": name,"capacity": capacity}        
        serializer = MothershipSerializer(data=item)
         
        if serializer.is_valid():            
            serializer.save()
            
            #create default ships
            code,msg = mothership_addShips(serializer.data["id"])            
            
            if code != 201:
                transaction.set_rollback(True)

            return code , serializer.data
        else:
            
            return status.HTTP_404_NOT_FOUND, ""
    except Exception as e:
        return status.HTTP_500_INTERNAL_SERVER_ERROR , {"error":e}   
    
def mothership_delete(id=None):
    try:
        if id == None or id == 0:    
            return status.HTTP_404_NOT_FOUND, {"error":"Id not found"} 
        else:
            item = Mothership.objects.get(pk=id)

            item.delete()

            msg = "Mothership " + str(id) + " deleted"       
            return status.HTTP_200_OK, {"msg":msg}  
    except Mothership.DoesNotExist:           
        return status.HTTP_400_BAD_REQUEST , {"error":"Mothership " + str(id) + " does not Exist"}


def mothership_remaining_capacity(mothership_ID):
    
    code, item = mothership_get(mothership_ID)
    
    if code == status.HTTP_200_OK:
        capacity = item["capacity"]
    else:
        capacity = 0
        
    count = Ship.objects.filter(mothership=mothership_ID).count()
   
    return capacity - count

def mothership_addShips(mothership_ID,ship_cant=settings.SHIP_DEFAULT):

    #validate capacity
    if mothership_remaining_capacity(mothership_ID) < int(ship_cant):
        msg = "The mothership " + str(mothership_ID) + " does not have enough capacity"
        return status.HTTP_400_BAD_REQUEST, {"error":msg}
        
    #create default ships
    for i in range(ship_cant):
        name =  "ship_" + ''.join(random.choice(string.ascii_uppercase) for _ in range(4))               
        newShip = {"alias": name,"capacity": settings.SHIP_CAPACITY ,"mothership": mothership_ID}
        code , msg = ship_create(newShip)

        if code != 200:
            return code , msg
        
    return status.HTTP_201_CREATED, {"msg":str(ship_cant) + " ships added"}   


def ship_get(id=None):
    try:
        if id == None:    
            mList = Ship.objects.all()
            serializer = ShipSerializer(mList,many=True)
        else:
            mList = Ship.objects.get(id=id)
            serializer = ShipSerializer(mList,many=False)
        
        return status.HTTP_200_OK , serializer.data
    except Ship.DoesNotExist:           
        return status.HTTP_400_BAD_REQUEST , {"error":"Ship " + str(id) + " does not Exist"}


@transaction.atomic
def ship_create(item=None):
    try:    
        serializer = ShipSerializer(data=item)
                
        if serializer.is_valid():            
            serializer.save()
                       
            #create default crew members
            for i in range(settings.CREW_DEFAULT):
                name =  names.get_full_name()
                code,msg = ship_addCrew(serializer.data["id"],name)            
                
                if code != 200:
                    transaction.set_rollback(True)
                    return code,{"error":msg}
                
            return code , serializer.data
        else:
            return status.HTTP_404_NOT_FOUND,{"error":"Mothership does not Exist"}
    except Exception as e:
        return status.HTTP_500_INTERNAL_SERVER_ERROR,{"error":e}
    
    
def ship_delete(id=None):
    try:
        if id == None or id == 0:    
            return status.HTTP_404_NOT_FOUND,""  
        else:
            item = Ship.objects.get(pk=id)

            item.delete()
        
            return status.HTTP_200_OK,""      
    except Exception as e:         
        return status.HTTP_500_INTERNAL_SERVER_ERROR,{"error":e}
    
def ship_remaining_capacity(ship_ID):
    
    code,item = ship_get(ship_ID)
    capacity = item["capacity"]
    
    count = Crew.objects.filter(ship=ship_ID).count()
   
    return capacity - count

def ship_is_member(ship_id,crew_name):
    
    if Crew.objects.filter(name=crew_name,ship=ship_id).count() == 1:
        return True
    else:
        return False

def ship_addCrew(ship,name):

    code, msg = ship_get(ship)
    if code != 200:
        msg = "Ship " + str(ship) + " does not exist"     
        return status.HTTP_404_NOT_FOUND,{"error":msg}

    #validate capacity
    remaining = ship_remaining_capacity(ship)    
    if remaining < 1:
        msg = "The ship " + str(ship) + " does not have enough capacity"
        return status.HTTP_400_BAD_REQUEST,{"error":msg}
    
    item = {"name": name,"ship": ship}
    code , msg = crew_create(item)

    return code , msg
     
def ship_switchCrew(crew_member,from_ship,to_ship):
    code, msg = ship_get(from_ship)
    if code != 200:
        msg = "Ship " + str(from_ship) + " does not exist"     
        return status.HTTP_404_NOT_FOUND,{"error":msg}
    
    code, msg = ship_get(to_ship)
    if code != 200:
        msg = "Ship " + str(to_ship) + " does not exist"     
        return status.HTTP_404_NOT_FOUND,{"error":msg}
        
    if not ship_is_member(from_ship,crew_member):
        msg = "Crew member " + crew_member +" is not on the ship " + str(from_ship)        
        return status.HTTP_400_BAD_REQUEST,{"error":msg}
    
    
    #validate capacity
    remaining = ship_remaining_capacity(to_ship)    
    if remaining < 1:
        msg = "The ship " + to_ship + "does not have enough capacity"
        return status.HTTP_400_BAD_REQUEST,{"error":msg}  
    else:  
        try:

            Crew.objects.filter(name=crew_member).update(ship = to_ship)

        except Exception as e:         
            return status.HTTP_500_INTERNAL_SERVER_ERROR,{"error":e}

    msg = "Crew member switched"
    return status.HTTP_200_OK,{"msg":msg}

def crew_get(id=None):
    try:
        if id == None:    
            mList = Crew.objects.all()
            serializer = CrewSerializer(mList,many=True)
        else:
            mList = Crew.objects.get(pk=id)
            serializer = CrewSerializer(mList,many=False)
        
        return status.HTTP_200_OK , serializer.data
    
    except Crew.DoesNotExist:           
        return status.HTTP_400_BAD_REQUEST , {"error":"Crew " + str(id) + " does not Exist"}
    
    
def crew_create(item=None):
    
    try:
        serializer = CrewSerializer(data=item)

        if serializer.is_valid():            
            serializer.save()
            
            return status.HTTP_200_OK , serializer.data
        else:
            return status.HTTP_404_NOT_FOUND , {"error":"Ship does not Exist"}
    except Exception as e:
        return status.HTTP_500_INTERNAL_SERVER_ERROR  , e      
    
    
def crew_delete(id=None):
    try:
        if id == None or id == 0:    
            return status.HTTP_404_NOT_FOUND , {"error":"Missing crew member"}
        else:
            item = Crew.objects.get(pk=id)

            item.delete()
        
            msg = "Crew member " + str(id) + " deleted"       
            return status.HTTP_200_OK, {"msg":msg}  
    except Crew.DoesNotExist:           
        return status.HTTP_400_BAD_REQUEST , {"error":"Crew " + str(id) + " does not Exist"}