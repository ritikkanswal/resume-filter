from django.urls import path
from . import views

urlpatterns = [
    path('',views.showformdata,name="home"),
    # path('add',views.add,name="add")
]