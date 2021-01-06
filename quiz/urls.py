from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('quiz/<str:slug>/',views.quiz_view,name='quiz'),
]
