from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product', views.add_product, name='add_product'),
    path('update_product', views.update_product, name='update_product'),
    path('delete_product', views.delete_product, name='delete_product')
]