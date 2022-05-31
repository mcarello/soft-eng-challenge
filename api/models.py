from django.db import models


class Mothership(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.pk}: {self.name}"


class Ship(models.Model):
    alias = models.CharField(max_length=50)
    capacity = models.IntegerField()
    mothership = models.ForeignKey(Mothership, on_delete=models.CASCADE, related_name='ship_mothership')
    
    def __str__(self) -> str:
        return f"{self.pk}:{self.alias}"
    
class Crew(models.Model):
    name = models.CharField(max_length=50)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE, related_name='crew_ship')
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"