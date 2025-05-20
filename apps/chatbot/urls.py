from django.urls import path
from .import views
from .views import *

urlpatterns = [
    path('chatbot/',views.chatbot ,name='chatbot'),
    path('chatbot/<str:subRoute>/', chatbotAPIViewContoller.as_view(), name='chatbot_api'),
    
]
