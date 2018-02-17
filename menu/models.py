# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Dishes(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, verbose_name='Название')
    nutrition_value = models.PositiveIntegerField(verbose_name='Пищевая ценность', default=0, blank=True, null=False)
    value = models.IntegerField(default=0, verbose_name='Цена', null=False, blank=False)
    image = models.ImageField(verbose_name='Изображение', upload_to='')

    def __str__(self):
        return 'Блюдо {}. Стоимость: {}'.format(self.name, self.value)
