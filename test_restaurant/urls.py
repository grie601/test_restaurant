"""test_restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from test_restaurant import settings
from django.contrib.staticfiles.urls import  static
import tastypie.api
from django.conf.urls import url, include
from django.contrib import admin

from api.api import DishResource
from menu import views

v_api = tastypie.api.Api(api_name='dish')
v_api.register(DishResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.all_menu),
    url(r'^add_dish/$', views.add_dish, name='add_dish'),
    url(r'^summary_value/$', views.summary_value, name='summary_value'),
    url(r'^api/', include(v_api.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)