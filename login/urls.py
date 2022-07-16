from django.urls import path
from .views import *

urlpatterns = [
    path('addUser/', AddUser.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('input/',Input_List.as_view()),
    path('input/<int:pk>/', Input_Detail.as_view()),
    path('Manual_weight/', Manual_List.as_view()),
    path('Manual_weight/<int:pk>/', Manual_Detail.as_view()),
    path('Direct_weight/', Direct_List.as_view()),
    path('Direct_weight/<int:pk>/', Direct_Detail.as_view()),
    path('quantity/', Quantity_List.as_view()),
    path('quantity/<int:pk>/', Quantity_Detail.as_view()),

]