
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/', views.item_list, name="item_list"),
    path('about/', views.about, name="about"),
    path('lost-item/', views.lost_item, name="lost_item"),
    path('found-item/', views.found_item, name="found_item"),
    path('report-lost-item/', views.report_lost_item, name='report_lost_item')
]
