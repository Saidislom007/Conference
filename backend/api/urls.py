from django.urls import path
from .views import *

urlpatterns =[
    path('get-all/',GetAll.as_view(),name='get-all'),
    path('<slug:slug>/', GetOne.as_view(), name='get-one'),
]