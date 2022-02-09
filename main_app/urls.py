from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # path('about/', views.About.as_view(), name="about"), # <- here we have added the new path
    path('cards/', views.CardList.as_view(), name="card_list"),
    path('cards/new/', views.CardCreate.as_view(), name="card_create"),
    path('cards/<int:pk>/', views.CardDetail.as_view(), name = "card_detail"),
    path('cards/<int:pk>/update', views.CardUpdate.as_view(), name = "card_update"),
    path('cards/<int:pk>/delete', views.CardDelete.as_view(), name="card_delete")
]

