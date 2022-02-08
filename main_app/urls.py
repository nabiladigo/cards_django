from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('about/', views.About.as_view(), name="about"), # <- here we have added the new path
    path('cards/', views.CardList.as_view(), name="card_list"),
    path('cards/new/', views.CardCreate.as_view(), name="card_create"),
    
]

