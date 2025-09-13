from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Guitar, GuitarForm, Category, Cart, Order, OrderStatus, CartItem, OrderItem
from django.urls import reverse_lazy

from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from cartapp.forms import BasketAddProductForm
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin


def main_page(request):
    return render(request, 'main_page.html')

def catalog_page(request):
    guitars = Guitar.objects.all() 
    return render(request, 'catalog.html', {'guitars': guitars})

def conatcts_page(request):
    return render(request, 'contacts.html')

@login_required
def cart(request):
    return render(request, 'cart.html')

def how_to_find(request):
    return render(request, 'how_to_find.html')

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

@login_required
def cabinet(request):
    user = request.user
    orders = Order.objects.filter(user=user).exclude(status__name="Завершен").order_by('-create_date')  
    context = {
        'user': user,
        'orders': orders,
    }
    return render(request, 'cab.html', context)


@login_required
def adminpanel(request):
    return render(request, 'admin_panel.html')


def category_detail(request, id):
    category = get_object_or_404(Category, pk=id)
    guitars = Guitar.objects.filter(category=category, is_exists=True)
    data = {
        'category': category,
        'guitars': guitars,
    }
    return render(request, 'category_detail.html', data)


#гитары
class GuitarListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_guitar'
    model = Guitar
    template_name = 'guitar/guitar_list.html'
    context_object_name = 'guitars'

class GuitarDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_guitar'
    model = Guitar
    template_name = 'guitar/guitar_detail.html'
    context_object_name = 'guitar'

class GuitarCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_guitar'
    model = Guitar
    template_name = 'guitar/guitar_form.html'
    fields = ['name', 'description', 'price', 'photo', 'in_shop_quantity', 'guitar_form', 'category', 'is_exists']
    success_url = reverse_lazy('guitar_list_view')

class GuitarUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_guitar'
    model = Guitar
    template_name = 'guitar/guitar_form.html'
    fields = ['name', 'description', 'price', 'photo', 'in_shop_quantity', 'guitar_form', 'category', 'is_exists']
    success_url = reverse_lazy('guitar_list_view')

class GuitarDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_guitar'
    model = Guitar
    template_name = 'guitar/guitar_confirm_delete.html'
    success_url = reverse_lazy('guitar_list_view')

#категории
class CategoryListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_category'
    model = Category
    template_name = 'category/category_list.html'
    context_object_name = 'categories'

class CategoryDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_category'
    model = Category
    template_name = 'category/category_detail.html'
    context_object_name = 'category'

class CategoryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_category'
    model = Category
    template_name = 'category/category_form.html'
    fields = ['name', 'photo', 'description']
    success_url = reverse_lazy('category_list_view')

class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_category'
    model = Category
    template_name = 'category/category_form.html'
    fields = ['name', 'photo', 'description']
    success_url = reverse_lazy('category_list_view')

class CategoryDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_category'
    model = Category
    template_name = 'category/category_confirm_delete.html'
    success_url = reverse_lazy('category_list_view')

#формы
class GuitarFormListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_guitarform'
    model = GuitarForm
    template_name = 'guitarform/guitarform_list.html'
    context_object_name = 'guitarforms'

class GuitarFormDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_guitarform'
    model = GuitarForm
    template_name = 'guitarform/guitarform_detail.html'
    context_object_name = 'guitarform'

class GuitarFormCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_guitarform'
    model = GuitarForm
    template_name = 'guitarform/guitarform_form.html'
    fields = ['name']
    success_url = reverse_lazy('guitarform_list_view')

class GuitarFormUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_guitarform'
    model = GuitarForm
    template_name = 'guitarform/guitarform_form.html'
    fields = ['name']
    success_url = reverse_lazy('guitarform_list_view')

class GuitarFormDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_guitarform'
    model = GuitarForm
    template_name = 'guitarform/guitarform_confirm_delete.html'
    success_url = reverse_lazy('guitarform_list_view')

#корзина
class CartListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_cart'
    model = Cart
    template_name = 'cart/cart_list.html'
    context_object_name = 'carts'

class CartDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_cart'
    model = Cart
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart'

class CartCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_cart'
    model = Cart
    template_name = 'cart/cart_form.html'
    fields = ['user']
    success_url = reverse_lazy('cart_list_view')

class CartUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_cart'
    model = Cart
    template_name = 'cart/cart_form.html'
    fields = ['user']
    success_url = reverse_lazy('cart_list_view')

class CartDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_cart'
    model = Cart
    template_name = 'cart/cart_confirm_delete.html'
    success_url = reverse_lazy('cart_list_view')

#заказ
class OrderListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_order'
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'

class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_order'
    model = Order
    template_name = 'order/order_detail.html'
    context_object_name = 'order'

class OrderCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_order'
    model = Order
    template_name = 'order/order_form.html'
    fields = ['address', 'total_price', 'user', 'status', 'first_name', 'last_name', 'middle_name', 'end_date']
    success_url = reverse_lazy('order_list_view')

class OrderUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_order'
    model = Order
    template_name = 'order/order_form.html'
    fields = ['address', 'total_price', 'user', 'status', 'first_name', 'last_name', 'middle_name', 'end_date']
    success_url = reverse_lazy('order_list_view')

class OrderDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_order'
    model = Order
    template_name = 'order/order_confirm_delete.html'
    success_url = reverse_lazy('order_list_view')

#статус
class StatusListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_orderstatus'
    model = OrderStatus
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'

class StatusDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_orderstatus'
    model = OrderStatus
    template_name = 'status/status_detail.html'
    context_object_name = 'status'

class StatusCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_orderstatus'
    model = OrderStatus
    template_name = 'status/status_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list_view')

class StatusUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_orderstatus'
    model = OrderStatus
    template_name = 'status/status_form.html'
    fields = ['name']
    success_url = reverse_lazy('status_list_view')

class StatusDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_orderstatus'
    model = OrderStatus
    template_name = 'status/status_confirm_delete.html'
    success_url = reverse_lazy('status_list_view')

#позиция в корзине
class CartItemListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_cartitem'
    model = CartItem
    template_name = 'cartitem/cartitem_list.html'
    context_object_name = 'cartitems'

class CartItemDetailView(DetailView):
    permission_required = 'shop.view_cartitem'
    model = CartItem
    template_name = 'cartitem/cartitem_detail.html'
    context_object_name = 'cartitem'

class CartItemCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_cartitem'
    model = CartItem
    template_name = 'cartitem/cartitem_form.html'
    fields = ['quantity', 'cart', 'guitar']
    success_url = reverse_lazy('cartitem_list_view')

class CartItemUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_cartitem'
    model = CartItem
    template_name = 'cartitem/cartitem_form.html'
    fields = ['quantity', 'cart', 'guitar']
    success_url = reverse_lazy('cartitem_list_view')

class CartItemDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_cartitem'
    model = CartItem
    template_name = 'cartitem/cartitem_confirm_delete.html'
    success_url = reverse_lazy('cartitem_list_view')


#позиция в заказе
class OrderItemListView(PermissionRequiredMixin, ListView):
    permission_required = 'shop.view_orderitem'
    model = OrderItem
    template_name = 'orderitem/orderitem_list.html'
    context_object_name = 'orderitems'

class OrderItemDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'shop.view_orderitem'
    model = OrderItem
    template_name = 'orderitem/orderitem_detail.html'
    context_object_name = 'orderitem'

class OrderItemCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shop.add_orderitem'
    model = OrderItem
    template_name = 'orderitem/orderitem_form.html'
    fields = ['quantity', 'price', 'guitar', 'order']
    success_url = reverse_lazy('orderitem_list_view')

class OrderItemUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shop.change_orderitem'
    model = OrderItem
    template_name = 'orderitem/orderitem_form.html'
    fields = ['quantity', 'price', 'guitar', 'order']
    success_url = reverse_lazy('orderitem_list_view')

class OrderItemDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shop.delete_orderitem'
    model = OrderItem
    template_name = 'orderitem/orderitem_confirm_delete.html'
    success_url = reverse_lazy('orderitem_list_view')


# подробная информация 
class GuitarOnClickDetailView(DetailView):
    model = Guitar
    template_name = 'guitar_detail_view.html'
    context_object_name = 'guitar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_basket'] = BasketAddProductForm()
        return context

# для авторизации регистрации и выхода

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:  
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                return redirect('catalog')
            else:
                return render(request, 'auth/login.html', context={'form': form}) 
        else:
            return render(request, 'auth/login.html', context={'form': form})
    else:
        form = LoginForm()
        return render(request, 'auth/login.html', context={'form': form})
    

def registration_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)  
        if form.is_valid():
            user = form.save() 
            login(request, user) 
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('catalog')
        else:
            return render(request, 'auth/registration.html', context={'form': form})
    else:
        form = RegistrationForm()
        return render(request, 'auth/registration.html', context={'form': form})
    

def logout_user(request):
    logout(request)
    return redirect('catalog')