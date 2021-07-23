from django.urls import path
from . import views


urlpatterns = [
    path('', views.ItemAPIView.as_view()),
    path('mobile/', views.CreateMobileView.as_view())
]
