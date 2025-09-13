from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [

   path('', main_page, name='main_page'),
   path('catalog/', catalog_page, name='catalog'),
   path('contacts/', conatcts_page, name='contacts'),
   path('how_to_find/', how_to_find, name='how_to_find'),
   path('categories/', categories, name='categories'),
   #path('cartuser/', cart, name='cart'),
   path('cabinet/', cabinet, name='cab'),
   path("categories/<int:id>/", category_detail, name='category_detail'),

   path('admindashboard/', adminpanel, name='adm'),

   path('guitar/', GuitarListView.as_view(), name='guitar_list_view'),
   path('guitar/<int:pk>/', GuitarDetailView.as_view(), name='guitar_detail_view'),
   path('guitar/create/', GuitarCreateView.as_view(), name='guitar_create_view'),
   path('guitar/<int:pk>/update/', GuitarUpdateView.as_view(), name='guitar_update_view'),
   path('guitar/<int:pk>/delete/', GuitarDeleteView.as_view(), name='guitar_delete_view'),

   path('category/', CategoryListView.as_view(), name='category_list_view'),
   path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail_view'),
   path('category/create/', CategoryCreateView.as_view(), name='category_create_view'),
   path('category/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update_view'),
   path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete_view'),

   path('guitarform/', GuitarFormListView.as_view(), name='guitarform_list_view'),
   path('guitarform/<int:pk>/', GuitarFormDetailView.as_view(), name='guitarform_detail_view'),
   path('guitarform/create/', GuitarFormCreateView.as_view(), name='guitarform_create_view'),
   path('guitarform/<int:pk>/update/',GuitarFormUpdateView.as_view(), name='guitarform_update_view'),
   path('guitarform/<int:pk>/delete/', GuitarFormDeleteView.as_view(), name='guitarform_delete_view'),

   path('cart/', CartListView.as_view(), name='cart_list_view'),
   path('cart/<int:pk>/', CartDetailView.as_view(), name='cart_detail_view'),
   path('cart/create/', CartCreateView.as_view(), name='cart_create_view'),
   path('cart/<int:pk>/update/', CartUpdateView.as_view(), name='cart_update_view'),
   path('cart/<int:pk>/delete/', CartDeleteView.as_view(), name='cart_delete_view'),

   path('order/', OrderListView.as_view(), name='order_list_view'),
   path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail_view'),
   path('order/create/', OrderCreateView.as_view(), name='order_create_view'),
   path('order/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update_view'),
   path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete_view'),

   path('status/', StatusListView.as_view(), name='status_list_view'),
   path('status/<int:pk>/', StatusDetailView.as_view(), name='status_detail_view'),
   path('status/create/', StatusCreateView.as_view(), name='status_create_view'),
   path('status/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update_view'),
   path('status/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete_view'),

   path('cartitem/', CartItemListView.as_view(), name='cartitem_list_view'),
   path('cartitem/<int:pk>/', CartItemDetailView.as_view(), name='cartitem_detail_view'),
   path('cartitem/create/', CartItemCreateView.as_view(), name='cartitem_create_view'),
   path('cartitem/<int:pk>/update/', CartItemUpdateView.as_view(), name='cartitem_update_view'),
   path('cartitem/<int:pk>/delete/', CartItemDeleteView.as_view(), name='cartitem_delete_view'),

   path('orderitem/', OrderItemListView.as_view(), name='orderitem_list_view'),
   path('orderitem/<int:pk>/', OrderItemDetailView.as_view(), name='orderitem_detail_view'),
   path('orderitem/create/', OrderItemCreateView.as_view(), name='orderitem_create_view'),
   path('orderitem/<int:pk>/update/', OrderItemUpdateView.as_view(), name='orderitem_update_view'),
   path('orderitem/<int:pk>/delete/', OrderItemDeleteView.as_view(), name='orderitem_delete_view'),


   path('choose_guitar/<int:pk>/', GuitarOnClickDetailView.as_view(), name='guitar_onclick_detail_view'),

   path('login/', login_user, name='login_user'),
   path('registration/', registration_user, name='registration_user'),
   path('logout/', logout_user, name='logout_user'),



]  

