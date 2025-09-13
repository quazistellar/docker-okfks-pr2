from .views import *
from rest_framework import routers

urlpatterns = [
]

router = routers.SimpleRouter()
router.register('guitar', GuitarViewSet, basename='guitar')
router.register('category', CategoryViewSet, basename='category')
router.register('guitarform', GuitarFormViewSet, basename='guitarform')
router.register('order', OrderViewSet, basename='order')
router.register('orderitem', OrderItemViewSet, basename='orderitem')
router.register('orderstatus', OrderStatusViewSet, basename='orderstatus')
router.register('cart', CartViewSet, basename='cart')
router.register('cartitem', CartItemViewSet, basename='cartitem')

urlpatterns += router.urls