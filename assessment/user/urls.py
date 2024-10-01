from django.urls import path
from .views import RequestAPIView

urlpatterns = [
    path('validate/', RequestAPIView.as_view(), name='validate')
]
