from django.shortcuts import render
from django.shortcuts import redirect
from apps.utils.enums import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging
from .services import *



logger = logging.getLogger(__name__)

def chatbot(request):
    return render(request,'admin/chatbot.html')


class chatbotAPIViewContoller(APIView):
    def __init__(self):
        self.service = chatBotServices()
        self.log =logging.getLogger(__name__)
        
    def get(self, request, subRoute=None):
        try:
            pass
        except Exception as err:
            logger.error('chatbot Controller Get Validation error: %s', str(err), exc_info=True)
            return Response({'status': ResStatus.error.value, 'message': 'chatbot Controller  error ' + str(err)}, 
                            status=status.HTTP_400_BAD_REQUEST)
      
            

    def post(self, request, api_version=None , subRoute=None, subdomain =None):
        try:
            
            if subRoute=='dify_chat':
                return self.service.chat_bot_dify(request)
            
            if subRoute=='chat':
                return self.service.chat_bot_grok(request)
              
        except Exception as err:
            logger.error('chatbot contoller exception: Required fields are empty: %s', str(err), exc_info=True)
            return Response({'status': ResStatus.error.value, 'message': 'chatbot contoller error ' + str(err)}, 
                            status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request, api_version=None , subRoute=None, subdomain =None):
        try:
            payload =request.data
            pass
                
            
        except Exception as err:

            logger.error('chatbot contoller exception: Required fields are empty: %s', str(err), exc_info=True)

            return Response({'status': ResStatus.error.value, 'message': 'chatbot failed with error ' + str(err)}, 
                            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, subRoute):
        try:
            
          pass
                
        except Exception as err:
            logger.error('chatbot contoller exception: Required fields are empty: %s', 
                        str(err), exc_info=True)

            return Response({'status': ResStatus.error.value, 
                            'message': 'chatbot contoller error ' + str(err)}, 
                            status=status.HTTP_400_BAD_REQUEST) 
    
    
    def delete(self, request, subRoute):
        try:
            pass
            
        except Exception as err:
            logger.error('chatbot contoller exception: Required fields are empty: %s', 
                        str(err), exc_info=True)

            return Response({'status': ResStatus.error.value, 
                            'message': 'chatbot contoller error ' + str(err)}, 
                            status=status.HTTP_400_BAD_REQUEST)    

