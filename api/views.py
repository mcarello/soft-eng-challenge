from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi
from . import services as s
from . import responses as schema
from rest_framework.decorators import api_view 
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from . import serializers as serializer 
from django.conf import settings
    
    
@swagger_auto_schema(method='get',operation_description="Get all the Mothership", responses=schema.mothership_list_response_schema)
@api_view(['GET'])
def mothership_list(request):   
    code , msg = s.mothership_get()
       
    return Response(data=msg ,status=code)


@swagger_auto_schema(methods=['delete'],operation_description="Delete a Mothership" ,responses=schema.mothership_delete_response_schema)
@swagger_auto_schema(methods=['get'],operation_description="Get Mothership detail", responses=schema.mothership_detail_response_schema)
@api_view(['GET','DELETE'])
def mothership_detail(request,pk):  
    
    if request.method == 'GET':
        code , mList = s.mothership_get(pk)
                         
        return Response(data=mList ,status=code)     
    
    elif request.method == 'DELETE':
        try:
            code,msg = s.mothership_delete(pk)
   
            return Response(msg,status=code)   
        
        except Exception as e: 
            return Response({'error_message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
        

@swagger_auto_schema(method='post',request_body=serializer.Mothership_Post_Request,operation_description="Create a Mothership", responses=schema.mothership_create_response_schema)        
@api_view(['POST'])
def mothership_add(request):    

    if not "name" in request.data:
        return Response({"error":"name parameter does not exist"},status=status.HTTP_400_BAD_REQUEST)
    
    name = request.data["name"]
    code , msg = s.mothership_create(name,settings.MOTHERSHIP_CAPACITY)
    
    return Response(msg,status=code)
    

@swagger_auto_schema(method='post',request_body=serializer.Mothership_Add_Ship_Request, operation_description="Add Ship to a Mothership", responses=schema.mothership_add_ship_response_schema)
@api_view(['POST'])
def mothership_add_ship(request):
    
    if not "mothership" in request.data or  not "ships" in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)
            
    code , msg = s.mothership_addShips(request.data["mothership"],int(request.data["ships"]))

    return Response(msg,status=code)
    
@swagger_auto_schema(method='get', operation_description="Get all the Ships", responses=schema.mothership_list_response_schema)
@api_view(['GET'])
def ship_list(request):
    code,mList = s.ship_get()
    
    return Response(data=mList ,status=code)    


@swagger_auto_schema(methods=['get'],operation_description="Get the details of a Ship", responses=schema.ship_detail_response_schema)
@swagger_auto_schema(methods=['delete'],operation_description="Delete a Ship" ,responses=schema.ship_delete_response_schema)
@api_view(['GET','DELETE'])
def ship_detail(request,pk):  
    if request.method == 'GET':
        code,mList = s.ship_get(pk)
            
        return Response(data=mList ,status=code)     
    
    elif request.method == 'DELETE':
        try:
            code,mList = s.ship_delete(pk)

            return Response(mList , status=code)
        except Exception as e: 
            return Response({'error_message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
          
@swagger_auto_schema(method='post',request_body=serializer.Ship_Create_Request,operation_description="Create a Ship", responses=schema.ship_create_response_schema)    
@api_view(['POST'])
def ship_create(request):    
        
    code,msg = s.ship_create(request.data)

    return Response(msg,status=code)
   
@swagger_auto_schema(method='post',request_body=serializer.Ship_Add_Member_Request,operation_description="Add crew member to a Ship", responses=schema.ship_add_member_response_schema)    
@api_view(['POST'])
def ship_add_crew(request):  
    
    if not "name" in request.data or  not "ship" in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    code,msg = s.ship_addCrew(request.data["ship"],request.data["name"])

    return Response(msg,status=code)
    
    
@swagger_auto_schema(method='post',request_body=serializer.Ship_Switch_Member_Request,operation_description="Switch a crew member to other Ship", responses=schema.ship_switch_member_response_schema)    
@api_view(['POST'])
def ship_switch_crew(request):  
    
    if not "crew_member" in request.data or  not "from_ship" in request.data or  not "to_ship" in request.data:
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    code,msg = s.ship_switchCrew(request.data["crew_member"],request.data["from_ship"],request.data["to_ship"])


    return Response(msg,status=code)

@swagger_auto_schema(method='get',operation_description="Get all the Crew Members", responses=schema.crew_list_response_schema)
@api_view(['GET'])
def crew_list(request):   
    code , mList = s.crew_get()
         
    return Response(data=mList ,status=code)

@swagger_auto_schema(methods=['get'],operation_description="Get details of a Crew Members", responses=schema.crew_detail_response_schema)
@swagger_auto_schema(methods=['delete'],operation_description="Get all the Crew Members",responses=schema.crew_delete_response_schema)
@api_view(['GET','DELETE'])
def crew_detail(request,pk):
    
    if request.method == 'GET':
        code, msg = s.crew_get(pk)
            
        return Response(msg,status=code)   
    
    elif request.method == 'DELETE':
        try:
            code,msg = s.crew_delete(pk)

            return Response(msg,status=code)  
        
        except Exception as e: 
            return Response({'error_message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 
            

@swagger_auto_schema(method='post',request_body=serializer.Crew_Post_Request, operation_description="Create a Crew member", responses=schema.crew_create_response_schema)
@api_view(['POST'])
def crew_create(request):  
            
    code , msg = s.crew_create(request.data)

    return Response(msg,status=code)