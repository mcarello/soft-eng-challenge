from rest_framework import serializers

from .models import Mothership,Ship,Crew

class MothershipSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Mothership
        fields = '__all__'
        
class ShipSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Ship
        fields = '__all__'
        
                
class CrewSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Crew
        fields = '__all__'              
 
        
class Crew_Post_Request(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ('name', 'ship')
        
class Crew_List_Request(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ('id','name', 'ship')        
        
class Mothership_Post_Request(serializers.ModelSerializer):
    class Meta:
        model = Mothership
        fields = ['name']
        
class Mothership_Add_Ship_Request(serializers.Serializer):  
        mothership = serializers.IntegerField()
        ships = serializers.IntegerField()
                
class Mothership_List_Request(serializers.ModelSerializer):
    class Meta:
        model = Mothership
        fields = ('id','name', 'capacity')         
        
class Ship_List_Request(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ('id','alias', 'capacity','mothership')       
        
class Ship_Create_Request(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields = ('alias', 'capacity','mothership')       
        
class Ship_Add_Member_Request(serializers.Serializer):  
        name = serializers.CharField()
        ship = serializers.IntegerField()
                        
class Ship_Switch_Member_Request(serializers.Serializer):  
        crew_member = serializers.CharField()
        from_ship = serializers.IntegerField()
        to_ship = serializers.IntegerField()
