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