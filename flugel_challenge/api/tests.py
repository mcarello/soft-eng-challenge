import names
from django.conf import settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .serializers import MothershipSerializer,ShipSerializer,CrewSerializer
from .models import Mothership,Ship,Crew

class TestApi(APITestCase):

    mothership = None

    def setUp(self):
        item = {"name": "ZXS978"}
        response = self.client.post(reverse('mothership_add'),data=item)
        self.mothership = MothershipSerializer(data=response.data)
                
        if self.mothership.is_valid():
            self.assertEqual(self.mothership.data["name"], "ZXS978")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        
        
    def test_create_mothership(self):
        """
        Testing UC: Given that the officer wants to add a mothership, when he adds a mothership, 
        then the mothership will be created with three ships
        """
        item = {"name": "RTT852"}
        response = self.client.post(reverse('mothership_add'),data=item)
        self.mothership = MothershipSerializer(data=response.data)
                
        if self.mothership.is_valid():           
            self.assertEqual(self.mothership.data["name"], "RTT852")
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Ship.objects.filter(mothership=1).count(), settings.SHIP_DEFAULT)
            
            
    def test_ship_members(self):
        """
        Testing UC: when the ship is created, then ship will create three crew members
        """
        self.assertEqual(Crew.objects.filter(ship=1).count(), settings.CREW_DEFAULT)            
            
    def test_add_ship_to_mothership(self):
        """
        Given that the officer wants to add a ship to a mothership, when he sends which mothership 
        and how much ships he wants to add, then ships will be created with three crew 
        members each one if the mothership contains less than 9 ships
        """
        item = {"mothership": "1","ships": 10}
        response = self.client.post(reverse('mothership_add_ship'),data=item)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


        count_ship_before = Ship.objects.filter(mothership=1).count()
        
        nro_ships = 2
        item = {"mothership": "1","ships": nro_ships}
        response = self.client.post(reverse('mothership_add_ship'),data=item)
        
        count_ship_after = Ship.objects.filter(mothership=1).count()
        self.assertEqual(count_ship_after , count_ship_before + nro_ships) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                                
        nro_ships = 5
        item = {"mothership": "1","ships": nro_ships}
        response = self.client.post(reverse('mothership_add_ship'),data=item)        
                                                
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_remove_ship(self):
        """
        Given that the officer wants to remove a ship, when he tries he send which ship 
        he wants to remove, then the ship will be removed along with all its crew members
        """
        
        ship_id = 1
        count_ship = Ship.objects.filter(id=ship_id).count()
        count_crew = Crew.objects.filter(ship=ship_id).count()
        self.assertEqual(count_crew, settings.CREW_DEFAULT)
                
        url = reverse('ship_detail',args=[ship_id])        
        response = self.client.delete(url)
           
        count_ship = Ship.objects.filter(id=ship_id).count()
        count_crew = Crew.objects.filter(ship=ship_id).count()
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        self.assertEqual(count_ship, 0)
        self.assertEqual(count_crew, 0)

        
        
    def test_add_crew_member(self):
        """
        Given that the officer wants to add a crew member, when he sends the name of the member 
        and the ship he wants to add, then the crew member is added if the ship contains less 
        than 5 crew members
        """        
        
        ship_id = 2
        name =  names.get_full_name()
        count_crew_before = Crew.objects.filter(ship=ship_id).count()
                
        item = {"name": name,"ship": ship_id}
        response = self.client.post(reverse('ship_add_crew'),data=item)
        
        count_crew_after = Crew.objects.filter(ship=ship_id).count()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(count_crew_before + 1, count_crew_after)
        
        for i in range(2):
            name =  names.get_full_name()
            item = {"name": name,"ship": ship_id}
            response = self.client.post(reverse('ship_add_crew'),data=item)
        
        count_crew_after = Crew.objects.filter(ship=ship_id).count()      

        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(count_crew_after, settings.SHIP_CAPACITY)
                
                
                
    def test_switch_member(self):
        """
        Given that the officer wants to switch a crew member between the ships, 
        when he sends the from_ship and the to_ship and the name of the crew member, 
        then the action will be allowed only if the to_ship will not exceed the capacity        
        """
        
        
        from_ship = 2
        to_ship = 3        
        crew_member_name = Crew.objects.filter(ship=from_ship).values('name').first()["name"]
         
        item = {"crew_member": crew_member_name,"from_ship": from_ship,"to_ship": to_ship}        
        response = self.client.post(reverse('ship_switch_crew'),data=item)
        
        crew_member_ship = Crew.objects.filter(name=crew_member_name).values('ship').first()["ship"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(to_ship, crew_member_ship)
        
    def test_mothership_list(self):
        
        response = self.client.get(reverse('mothership_list'))
        self.mothership = MothershipSerializer(data=response.data)
                
        if self.mothership.is_valid():
            item = [{"id": 1,"name": "ZXS978","capacity": settings.MOTHERSHIP_CAPACITY}]
            self.assertEqual(self.mothership.data, item)
            self.assertEqual(len(response.data),1)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
  
    def test_mothership_detail(self):
        url = reverse('mothership_detail',args=[1])        
        response = self.client.get(url)
           
        item = {"id": 1,"name": "ZXS978","capacity": settings.MOTHERSHIP_CAPACITY}
        self.assertEqual(response.data, item)
        self.assertEqual(200, status.HTTP_200_OK)
        

    def test_ship_list(self):        
        response = self.client.get(reverse('ship_list'))
        self.assertEqual(len(response.data), settings.SHIP_DEFAULT)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_crew_list(self):        
        response = self.client.get(reverse('crew_list'))
        self.assertEqual(len(response.data), 9)
        self.assertEqual(response.status_code, status.HTTP_200_OK)