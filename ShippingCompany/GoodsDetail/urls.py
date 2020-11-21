from django.urls import path
from . import views
from .views import GoodsDetailView

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('<int:pk>/goodsdetail', GoodsDetailView.as_view(), name='products')
]
