from django.urls import path
from .views import BlackAndWhite, Blur

urlpatterns = [
    path('bw/', BlackAndWhite.as_view()),
    path('blur/', Blur.as_view()),
]
