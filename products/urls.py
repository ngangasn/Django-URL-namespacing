from django.urls import path

from .views import products, product

app_name = 'products'
urlpatterns = [
    path('', products, name='list'),
    path('<int:id>/', product, name='detail'),
]
