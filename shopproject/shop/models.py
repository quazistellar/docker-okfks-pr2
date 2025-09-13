from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


MAX_LENGTH = 255

class GuitarForm(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название формы гитары', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма гитары'
        verbose_name_plural = 'Формы гитар'

class Category(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название категории гитар', unique=True)
    photo = models.ImageField(upload_to='photos', verbose_name='Фотография')
    description = models.TextField(null=True, blank=True, verbose_name='Описание категории')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория гитары'
        verbose_name_plural = 'Категории гитар'

class Guitar(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название гитары', unique=True)
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена', validators=[MinValueValidator(0.0)])
    photo = models.ImageField(upload_to='photos', verbose_name='Фотография')
    in_shop_quantity = models.PositiveIntegerField(default=0, verbose_name='Количество на складе')
    guitar_form = models.ForeignKey(GuitarForm, on_delete=models.PROTECT, verbose_name='Форма гитары')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность к заказу')

    def __str__(self):
        return f"{self.name} - ({self.price} рублей.)"

    class Meta:
        verbose_name = 'Гитара'
        verbose_name_plural = 'Гитары'

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', unique=True)

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name='Корзина')
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE, verbose_name='Гитара')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f"{self.guitar.name} x {self.quantity} в корзине"

    class Meta:
        verbose_name = 'Позиция в корзине'
        verbose_name_plural = 'Позиции в корзине'
        unique_together = ('cart', 'guitar')

class OrderStatus(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название статуса', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказов'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT, verbose_name='Статус')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    address = models.TextField(verbose_name="Адрес доставки")
    comment = models.TextField(max_length=MAX_LENGTH, null=True, blank=True, verbose_name="Комментарий к заказу")
    total_price = models.FloatField(default=0.0, verbose_name='Общая сумма', validators=[MinValueValidator(0.0)])
    
    first_name = models.CharField(max_length=100, verbose_name='Имя покупателя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия покупателя')
    middle_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Отчество покупателя')
    end_date = models.DateTimeField(null=True, blank=True, verbose_name='Дата окончания заказа')

    def __str__(self):
        return f"Заказ {self.id} от {self.user.username}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    guitar = models.ForeignKey(Guitar, on_delete=models.PROTECT, verbose_name='Гитара')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')
    price = models.FloatField(verbose_name='Цена на момент заказа', validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.guitar.name} x {self.quantity} в заказе {self.order.id}"

    class Meta:
        verbose_name = 'Позиция в заказе'
        verbose_name_plural = 'Позиции в заказах'
        unique_together = ('order', 'guitar')