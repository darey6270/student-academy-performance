from django.urls import path

from .views import *


urlpatterns = (
    path('', HomeWebsite.as_view(), name='index'),
    path('about/', AboutWebsite.as_view(), name="about"),
    path('contact/', ContactWebsite.as_view(), name="contact"),
    path('service/', PredictionPage, name="service"),
    #path('predict/<str:predict_text>/', PredictWebsite.as_view(), name="predict"),
)


