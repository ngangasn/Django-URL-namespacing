from django.urls import path

from .views import index, article

app_name = 'blog'
urlpatterns = [
    path('', index, name='list'),
    path('<int:id>/', article,),
]
