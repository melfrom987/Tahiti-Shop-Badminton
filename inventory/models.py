from django.db import models
import uuid
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(default="Description par défaut")
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    color = models.CharField(max_length=100, default="Couleur par défaut")
    type_pro = models.CharField(max_length=255, default="Type par défaut")
    image = models.ImageField(upload_to='accessory_images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Grip(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(default="Description par défaut")
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    color = models.CharField(max_length=100, default="Couleur par défaut")
    image = models.ImageField(upload_to='shoe_images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Shoe(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(default="Description par défaut")
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    color = models.CharField(max_length=100, default="Couleur par défaut")
    size_39_quantity = models.IntegerField(default=0)
    size_40_quantity = models.IntegerField(default=0)
    size_41_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='shoe_images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class String(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(default="Description par défaut")
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    type_pro = models.CharField(max_length=255, default="Type par défaut")
    image = models.ImageField(upload_to='string_images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Bag(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(default="Description par défaut")
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    color = models.CharField(max_length=50, default="Couleur par défaut")
    size = models.CharField(max_length=50, default="Taille par défaut")
    image = models.ImageField(upload_to='bag_images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Racket(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(default="Description par défaut")
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    type_pro = models.CharField(max_length=255, default="Type par défaut")
    image = models.ImageField(upload_to='racket_images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Clothe(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(default="Description par défaut")
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    color = models.CharField(max_length=100, default="Couleur par défaut")
    type_pro = models.CharField(max_length=255, default="Type par défaut")
    size_M_quantity = models.IntegerField(default=0)
    size_L_quantity = models.IntegerField(default=0)
    size_XL_quantity = models.IntegerField(default=0)
    size_2XL_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='clothe_images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Shuttle(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    description = models.TextField(default="Description par défaut")
    quantity = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    type_pro = models.CharField(max_length=255, default="Type par défaut")
    image = models.ImageField(upload_to='shuttle_images/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(default=1)
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.quantity * self.content_object.price

    def __str__(self):
        return f"{self.quantity} of {self.content_object.name} in cart"

##

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')

    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity})"

class OrderItem(models.Model):
    order = models.ForeignKey('Order', related_name='items', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, default=1)
    object_id = models.PositiveIntegerField(default=1)
    product = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.order} - {self.product} ({self.quantity})"

