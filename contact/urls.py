from django.urls import path
from . import views


app_name='contact'

urlpatterns =[
    path('',views.page,name='index'),
    path('search/',views.search,name='search'),
    
    # Contact CRUD
    path('contact/<int:id>/detail/',views.create,name='contact'),


]


