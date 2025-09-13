from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from shop.models import Guitar, Order, OrderItem, OrderStatus
from cartapp.cart import Basket
from .forms import OrderForm, BasketAddProductForm
from django.conf import settings

#для почты (работает только локально)
import urllib.request
import urllib.parse
from django.http import HttpResponseServerError

@login_required
def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/basket_detail.html', {'basket': basket})

@login_required
def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Guitar, pk=product_id)
    basket.remove(product)
    return redirect('basket_detail')

@login_required
def basket_clear(request):
    basket = Basket(request)
    basket.clear()
    return redirect('basket_detail')

@require_POST
def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Guitar, pk=product_id)
    form = BasketAddProductForm(request.POST)
    if form.is_valid():
        basket.add(product=product, count=form.cleaned_data['quantity'])
    return redirect('basket_detail')

@login_required
def basket_decrement(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Guitar, pk=product_id)
    basket.decrement(product)
    return redirect('basket_detail')

@login_required
def basket_increment(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Guitar, pk=product_id)
    current_quantity = basket.basket.get(str(product_id), {'quantity': 0})['quantity']
    if current_quantity >= 30: 
        return redirect('basket_detail') 
    basket.add(product=product, count=1)
    return redirect('basket_detail')


@login_required
def open_order(request):
    basket = Basket(request)
    total_price = 0
    items_list = []

    if len(basket) == 0:
        return redirect('basket_detail')

    for item in basket:
        guitar = item['guitar']
        quantity = item['quantity']
        item_price = guitar.price * quantity
        total_price += item_price
        items_list.append({'name': guitar.name, 'quantity': quantity, 'price': guitar.price})

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            initial_status, created = OrderStatus.objects.get_or_create(name='В обработке')
            quantity_error = False
            error_context = None
            for item in basket:
                guitar = item['guitar']
                quantity = item['quantity']
                if guitar.in_shop_quantity < quantity:
                    error_context = {
                        'error_message': f"Недостаточно товара {guitar.name} на складе. Доступно всего {guitar.in_shop_quantity}!",
                        'guitar_name': guitar.name,
                        'available_quantity': guitar.in_shop_quantity,
                    }
                    quantity_error = True
                    break
            if quantity_error:
                return render(request, 'order/error_quantity.html', error_context, status=400)

            address = form.cleaned_data['address']

            order = Order(
                user=request.user,
                status=initial_status,
                address=address,
                comment=form.cleaned_data['comment'],
                total_price=total_price,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                middle_name=form.cleaned_data['middle_name'],
            )
            order.save()

            try:
                for item in basket:
                    guitar = item['guitar']
                    quantity = item['quantity']
                    OrderItem.objects.create(
                        order=order,
                        guitar=guitar,
                        quantity=quantity,
                        price=guitar.price
                    )
                    guitar.in_shop_quantity -= quantity
                    guitar.save()
            except Exception as e:
                order.delete()
                print(f"Ошибка при создании заказа: {e}")
                return render(request, 'order/error_quantity.html', {'error_message': 'Произошла ошибка при создании заказа!'}, status=500)

            basket.clear()

            try:
                context = {
                    'username': request.user.username,
                    'total_price': total_price,
                    'items_list': items_list,
                    'address': address
                }

                items_text = "\n".join([f"- {item['name']} (x{item['quantity']}) по цене {item['price']} руб." for item in context['items_list']])
                message = f"""Спасибо за ваш заказ, {context['username']}!

Ваш заказ на сумму {context['total_price']} руб. по адресу {context['address']} успешно оформлен.

Состав заказа:
{items_text}

Если у вас возникли вопросы, напишите нам - guiznotes@mail.ru.
"""
                api_url = settings.EMAIL_API_URL

                data = {
                    'recipient': request.user.email,
                    'subject': 'GuizNotes - заказ успешно оформлен!',
                    'body': message,
                }

                data = urllib.parse.urlencode(data).encode('utf-8')

                try:
                    req = urllib.request.Request(api_url, data=data, method='POST')
                    with urllib.request.urlopen(req) as response:
                        if response.getcode() == 200:
                            print("Письмо отправлено!")
                        else:
                            print(f"Ошибка при отправке письма: {response.getcode()} - {response.read().decode('utf-8')}")

                except urllib.error.URLError as e:
                    print(f"Ошибка при отправке письма: {e}")


            except Exception as e:
                print(f"Ошибка при подготовке/отправке письма: {e}")

            return redirect('basket_detail')
        else:
            return render(
                request,
                'order/order_buy_form.html',
                {'form': form, 'basket': items_list, 'total_price': total_price}
            )
    else:
        form = OrderForm()

    return render(
        request,
        'order/order_buy_form.html',
        {'form': form, 'basket': items_list, 'total_price': total_price}
    )
