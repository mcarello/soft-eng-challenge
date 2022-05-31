from django.urls import path 
from . import views

urlpatterns = [

    path('motherships/', views.mothership_list , name='mothership_list'  ),
    path('mothership/<int:pk>', views.mothership_detail , name='mothership_detail' ),
    path('mothership/', views.mothership_add , name='mothership_add'),
    path('mothership/add_ship', views.mothership_add_ship, name='mothership_add_ship' ),
    
    path('ships/', views.ship_list , name='ship_list'  ),
    path('ship/<int:pk>', views.ship_detail , name='ship_detail'  ),
    path('ship/', views.ship_create , name='ship_create'  ),
    path('ship/add_crew', views.ship_add_crew , name='ship_add_crew'  ),
    path('ship/switch_crew', views.ship_switch_crew , name='ship_switch_crew'  ),   
    
    path('crews/', views.crew_list  , name='crew_list'  ),  
    path('crew/<int:pk>', views.crew_detail  , name='crew_detail'  ),  
    path('crew/', views.crew_create  , name='crew_create'  ),         
]
