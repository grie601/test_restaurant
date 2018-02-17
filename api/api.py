import os

from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from menu.models import Dishes


class DishResource(ModelResource):
    class Meta:
        queryset = Dishes.objects.all()
        resource_name = 'dishes'
        authorization = Authorization()
        allowed_methods = ['get', 'post']

    def deserialize(self, request, data, format='application/json'):
        FILE_STORAGE = os.path.join(os.path.dirname(__file__), 'images/')
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')
        if format.startswith('multipart') and request.FILES:
            data = request.POST.copy()
            # data['file'] = default_storage.save('{}{}'.format(FILE_STORAGE, request.FILES['image']),
            #                                     ContentFile(request.FILES['image'].read()))
            dish = Dishes()
            name = data.get('name', '')
            nutrition_value = data.get('nutrition_value', '')
            value = data.get('value', '')
            if name != '' and value != '' and nutrition_value != '':
                dish.name = name
                dish.image = request.FILES['image']
                dish.value = value
                dish.nutrition_value = nutrition_value
                # dish.save()
                data.update(request.FILES)
            return data
        return super(DishResource, self).deserialize(request, data, format)
