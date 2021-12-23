from django.urls import path
from src import views

urlpatterns = [
    path('', views.home, name='src-home'),
    path('<id>/', views.detail, name='src-detail')
]
