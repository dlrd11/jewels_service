from django.urls import path
from .views import JewelListCreateView, JewelDetailView

urlpatterns = [
    path('jewels/', JewelListCreateView.as_view(), name='jewel-list-create'),
    path('jewels/<int:pk>/', JewelDetailView.as_view(), name='jewel-detail'),
]
