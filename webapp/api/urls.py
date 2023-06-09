from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('register/', views.Register.as_view(), name="register"),
    path('retrieve/', views.Retrieve.as_view(), name="retrieve"),
    path('newdoc/', views.Newdoc.as_view(), name="newdoc"),
]