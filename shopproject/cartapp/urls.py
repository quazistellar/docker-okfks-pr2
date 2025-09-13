from django.urls import path
from .views import *

urlpatterns = [
    path('', basket_detail, name='basket_detail'),
    path('remove/<int:product_id>/', basket_remove, name='basket_remove'),
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('clear/', basket_clear, name='basket_clear'),
    path('create_order/', open_order, name='open_order'),
    
    path('basket/decrement/<int:product_id>/', basket_decrement, name='basket_decrement'),  
    path('basket/increment/<int:product_id>/', basket_increment, name='basket_increment'), 
]