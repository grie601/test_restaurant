# -*- coding: utf-8 -*-
import os


from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import render


from menu.forms import AddDish
from menu.models import Dishes

# Create your views here.


def all_menu(request):
    args = {}
    # req = request.GET
    # if req:
    args['menu'] = Dishes.objects.all()
    args['path'] = 'E:/Working/Python/test_restaurant/'
    return render(request, 'Menu.html', args)


def add_dish(request):
    args = {}
    FILE_STORAGE = os.path.join(os.path.dirname(__file__), 'images/')
    req = request.POST

    if req:
        f = AddDish(req)
        # file = ModelFormWithFileField()
        if f.is_valid():
            data = f.cleaned_data
            new_dish = Dishes(name=data['name_dish'],
                              nutrition_value=data['nutrition_value'],
                              value=data['value'],
                              image=request.FILES['image'])

            new_dish.save()
            args['response'] = 'The Dish was added'
        else:
            args['response'] = 'The Dish wasnt added. Insert error!'

    args['AddDish'] = AddDish()

    return render(request, 'Add_Dish.html', args)


def summary_value(request):
    args = {}
    req = request.GET
    args['count'] = 0
    args['all_choose_dishes'] = []
    if req:
        elements = [req.get(dish) for dish in req if 'dish' in dish]
        for elem in elements:
            menu_elem = Dishes.objects.get(id=elem)
            args['count'] += menu_elem.value
            args['all_choose_dishes'].append(menu_elem)
        args['response'] = 'Your FULL check cost: {}'.format(args['count'])
    if args['count'] == 0:
        args['response'] = 'Your check is empty. Check IT'
    return render(request, 'summary_value.html', args)