from django.urls import path 
from .views import HomePageView,GetOrderView,PlaceOrderView,AddFoodView,DetailFoodView,EditFoodView,DeleteFoodView,PlacedOrderView,ChiefOrderView,HomefrstView,HomesecView

urlpatterns = [
    path('',HomefrstView,name='home'),
    path('table2',HomesecView,name='home1'),
    path('emenu/<int:tab_no>',HomePageView,name='emenu'),
    path('get_order/<str:name>/<int:price>/<int:tab_no>',GetOrderView,name='getorder'),
    path('ordered/<int:tab_no>',PlaceOrderView,name='placeorder'),
    path('add_item',AddFoodView.as_view(),name='additem'),
    path('food_detail/<int:pk>',DetailFoodView.as_view(),name='detailfood'),
    path('update_food/<int:pk>',EditFoodView.as_view(),name='updatefood'),
    path('delete_food/<int:pk>',DeleteFoodView.as_view(),name='deletefood'),
    path('placedorder/<int:tab_no>',PlacedOrderView,name='placedorder'),
    path('chief_order',ChiefOrderView,name='chieforder'),
]