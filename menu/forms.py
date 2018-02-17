# -*- coding: utf-8 -*-
from django import forms

class AddDish(forms.Form):
    name_dish = forms.CharField(initial='',label='название блюда', required=True)
    nutrition_value = forms.CharField(initial='', label='пищевая ценность', required=True)
    value = forms.IntegerField(min_value=1, max_value=50000, label='Цена', required=True)
    image = forms.ImageField(label='Изображение', required=False)


