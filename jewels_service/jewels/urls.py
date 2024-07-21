from django.urls import path
from .views import JewelView

urlpatterns = [
    path('jewels/', JewelView.as_view(), name='jewels-read'),
    path('jewels/<int:pk>/', JewelView.as_view(), name='jewels-api'),
]
