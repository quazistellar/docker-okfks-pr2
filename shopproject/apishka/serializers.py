from rest_framework import serializers
from shop.models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'photo', 'description']

class GuitarFormSerializers(serializers.ModelSerializer):
    class Meta:
        model = GuitarForm
        fields = ['name']

class GuitarSerializers(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=15, decimal_places=2)
    class Meta:
        model = Guitar
        fields = ['id', 'name', 'description', 'price', 'photo', 'in_shop_quantity', 'guitar_form', 'category', 'is_exists'] 
        

class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'guitar', 'quantity'] 

class OrderStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = ['name'] 

class OrderSerializers(serializers.ModelSerializer):
    total_price = serializers.DecimalField(label='Цена', max_digits=15, decimal_places=2)
    class Meta:
        model = Order
        fields = ['user', 'status', 'create_date', 'address', 'comment', 'total_price', 'first_name', 'last_name', 'middle_name', 'end_date']

class OrderItemSerializers(serializers.ModelSerializer):
    price = serializers.DecimalField(label='Цена', max_digits=15, decimal_places=2)
    class Meta:
        model = OrderItem
        fields = ['order', 'guitar', 'quantity', 'price'] 

