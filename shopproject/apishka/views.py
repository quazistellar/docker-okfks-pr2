from .serializers import *
from rest_framework import viewsets, mixins
from shop.models import *
from .permission import *
from .permission import PaginationPage

class GuitarViewSet(viewsets.ModelViewSet):
    queryset = Guitar.objects.all()
    serializer_class = GuitarSerializers
    # permission_classes = [CustomPermission]
    # pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Guitar.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif description is not None:
            queryset = queryset.filter(description__icontains=description)

        return queryset
        

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif description is not None:
            queryset = queryset.filter(description__icontains=description)

        return queryset

class GuitarFormViewSet(viewsets.ModelViewSet):
    queryset = GuitarForm.objects.all()
    serializer_class = GuitarFormSerializers
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = GuitarForm.objects.all()
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset

class CartViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Cart.objects.all()
        user_id = self.request.query_params.get('user', None) 

        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)  

        return queryset


class CartItemViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = CartItem.objects.all()
        cart_id_str = self.request.query_params.get('cart', None) 

        if cart_id_str is not None:
            cart_id = int(cart_id_str)  
            queryset = queryset.filter(cart_id=cart_id)  

        return queryset

class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializers
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = OrderStatusViewSet.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = Order.objects.all()
        name = self.request.query_params.get('status', None)
        description = self.request.query_params.get('last_name', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        elif description is not None:
            queryset = queryset.filter(description__icontains=description)

        return queryset

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializers
    permission_classes = [CustomPermission]
    pagination_class = PaginationPage

    def get_queryset(self):
        queryset = OrderItem.objects.all()
        guitar_id_str = self.request.query_params.get('guitar', None)  

        if guitar_id_str is not None:
            guitar_id = int(guitar_id_str) 
            queryset = queryset.filter(guitar_id=guitar_id)  

        return queryset