from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:write>/',views.detail, name='detail')
]