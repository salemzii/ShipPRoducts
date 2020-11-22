from django.urls import path
from . import views
from .views import GoodsDetailView

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('<int:pk>/GoodsDetail', GoodsDetailView.as_view(), name='products')
]
