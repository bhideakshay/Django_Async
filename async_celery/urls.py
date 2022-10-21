from django.urls import path
from .views import MyView

urlpatterns = [
    path('send-async-email/', MyView.as_view()),
]