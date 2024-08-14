from django.urls import path
from .views import *
urlpatterns = [
    path('historyNA/<str:pk>/', NotAllowedSearchAPIView.as_view()),
]