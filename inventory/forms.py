from django import forms
from .models import Shoe, Clothe, Bag, Shuttle, Accessory, String, Racket
from django.forms import modelformset_factory
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# ADD FORM
class AccessoryForm(forms.ModelForm):
    class Meta:
        model = Accessory
        fields = ['name', 'price', 'description', 'type_pro', 'quantity', 'image', 'color']
        widgets = {
            'name' : forms.TextInput(attrs={'required': True}),
            'price': forms.NumberInput(attrs={'required': True}),
            'description' : forms.TextInput(attrs={'required': True}),
            'quantity': forms.NumberInput(attrs={'required': True}),
            'type_pro': forms.TextInput(attrs={'required': True}),
            'color': forms.TextInput(attrs={'required': True}),
        }

class ShoeForm(forms.ModelForm):
    class Meta:
        model = Shoe
        fields = ['name', 'price', 'description', 'quantity', 'image', 'color', 'size_39_quantity', 'size_40_quantity', 'size_41_quantity']
        widgets = {
            'name' : forms.TextInput(attrs={'required': True}),
            'price': forms.NumberInput(attrs={'required': True}),
            'description' : forms.TextInput(attrs={'required': True}),
            'quantity': forms.NumberInput(attrs={'required': True}),
            'color': forms.TextInput(attrs={'required': True}),
            'size_39_quantity': forms.NumberInput(attrs={'required': True}),
            'size_40_quantity': forms.NumberInput(attrs={'required': True}),
            'size_41_quantity': forms.NumberInput(attrs={'required': True}),
        }

class StringForm(forms.ModelForm):
    class Meta:
        model = String
        fields = ['name', 'price', 'description', 'quantity', 'image', 'type_pro']
        widgets = {
            'name' : forms.TextInput(attrs={'required': True}),
            'price': forms.NumberInput(attrs={'required': True}),
            'description' : forms.TextInput(attrs={'required': True}),
            'quantity': forms.NumberInput(attrs={'required': True}),
            'type_pro': forms.TextInput(attrs={'required': True}),
        }

class GripForm(forms.ModelForm):
    class Meta:
        model = String
        fields = ['name', 'price', 'description', 'quantity', 'image', 'type_pro']
        widgets = {
            'name' : forms.TextInput(attrs={'required': True}),
            'price': forms.NumberInput(attrs={'required': True}),
            'description' : forms.TextInput(attrs={'required': True}),
            'quantity': forms.NumberInput(attrs={'required': True}),
            'type_pro': forms.TextInput(attrs={'required': True}),
        }

class BagForm(forms.ModelForm):
    class Meta:
        model = Bag
        fields = ['name', 'price', 'description', 'quantity', 'image', 'color', 'size']
        widgets = {
            'name' : forms.TextInput(attrs={'required': True}),
            'price': forms.NumberInput(attrs={'required': True}),
            'description' : forms.TextInput(attrs={'required': True}),
            'quantity': forms.NumberInput(attrs={'required': True}),
            'color': forms.TextInput(attrs={'required': True}),
            'size': forms.TextInput(attrs={'required': True}),
        }

class RacketForm(forms.ModelForm):
    class Meta:
        model = Racket
        fields = ['name', 'price', 'description', 'quantity', 'image', 'type_pro']
        widgets = {
            'name' : forms.TextInput(attrs={'required': True}),
            'price': forms.NumberInput(attrs={'required': True}),
            'description' : forms.TextInput(attrs={'required': True}),
            'quantity': forms.NumberInput(attrs={'required': True}),
            'type_pro': forms.TextInput(attrs={'required': True}),
        }

class ClotheForm(forms.ModelForm):
    class Meta:
        model = Clothe
        fields = ['name', 'price', 'description', 'quantity', 'image', 'color', 'type_pro', 'size_M_quantity', 'size_L_quantity', 'size_XL_quantity', 'size_2XL_quantity']
        widgets = {
            'name' : forms.TextInput(attrs={'required': True}),
            'price': forms.NumberInput(attrs={'required': True}),
            'description' : forms.TextInput(attrs={'required': True}),
            'quantity': forms.NumberInput(attrs={'required': True}),
            'color': forms.TextInput(attrs={'required': True}),
            'type_pro': forms.TextInput(attrs={'required': True}),
            'size_M_quantity': forms.NumberInput(attrs={'required': True}),
            'size_L_quantity': forms.NumberInput(attrs={'required': True}),
            'size_XL_quantity': forms.NumberInput(attrs={'required': True}),
            'size_2XL_quantity': forms.NumberInput(attrs={'required': True}),
        }

class ShuttleForm(forms.ModelForm):
    class Meta:
        model = Shuttle
        fields = ['name', 'price', 'description', 'quantity', 'image', 'type_pro']
        widgets = {
            'name' : forms.TextInput(attrs={'required': True}),
            'price': forms.NumberInput(attrs={'required': True}),
            'description' : forms.TextInput(attrs={'required': True}),
            'quantity': forms.NumberInput(attrs={'required': True}),
            'type_pro': forms.TextInput(attrs={'required': True}),
        }

