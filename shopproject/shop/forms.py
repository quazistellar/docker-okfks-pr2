from django import forms
from .models import Guitar, GuitarForm, Order, OrderItem, OrderStatus, Cart, CartItem, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class GuitarModelForm(forms.ModelForm):
    class Meta:
        model = Guitar
        fields = ['name', 'description', 'price', 'photo', 'in_shop_quantity', 'is_exists', 'category', 'guitar_form']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'photo', 'description']

class GuitarFormForm(forms.ModelForm):
    class Meta:
        model = GuitarForm
        fields = ['name']


class Order(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'total_price', 'user', 'status', 'first_name', 'last_name', 'middle_name', 'end_date']


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['user']

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = ['name']
        widgets = {'name' : forms.TextInput(attrs={'class': 'form-control'})}

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity', 'cart', 'guitar']

class OrderitemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity', 'price', 'guitar', 'order']
      

#для авторизации и регистрации

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control dark-input'}),
        min_length=2
    )
    email = forms.CharField(
        label='Электронная почта',
        widget=forms.EmailInput(attrs={'class': 'form-control dark-input'}),
    )
    password1 = forms.CharField(
        label='Придумайте пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control dark-input'}),
    )
    password2 = forms.CharField(
        label='Повторите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control dark-input'}),
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control dark-input'}),
    )
    password = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control dark-input'}),
    )
