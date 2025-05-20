# python builtins
import logging
import logging.config
from rest_framework.response import Response
from rest_framework import status
from apps.utils.enums import *
from .models import *
import requests

logger = logging.getLogger(__name__)
# GROQ_API_KEY = os.getenv("GROQ_API_KEY") 
from decouple import config
GROQ_API_KEY = config('GROQ_API_KEY')  

print("GROQ_API_KEY", GROQ_API_KEY)



class chatBotServices(object):
    def __init__(self):
        self.log =logging.getLogger(__name__)
        
    def chat_bot_dify(self, request):
        try:
            # import pdb;
            # pdb.set_trace()
            payload = request.data
            user_message = payload.get('message')
            conversation_id = payload.get('conversation_id')
            if not user_message:
                raise ValueError('Message is required.')

            # Call Dify API
            headers = {
                'Authorization': 'Bearer app-KQNmZMPxVgS1RVZLTfMrNp7n',  # Replace with your actual API key
                'Content-Type': 'application/json',
            }
            
        
            dify_payload={
            "query": user_message,
            "inputs": {},
            "response_mode": "blocking",
            "user": "user-001",
            "conversation_id": conversation_id if conversation_id else ""
            }

            response = requests.post(
                'https://api.dify.ai/v1/chat-messages',
                headers=headers,
                json=dify_payload
            )

            if response.status_code != 200:
                raise Exception(f"Dify API error: {response.text}")

            dify_response = response.json()

            return Response({
                'status': 'success',
                'response': dify_response.get('answer', 'No answer received'),  # adapt based on actual structure
                'conversation_id': dify_response.get('conversation_id', 'no conversation_id'), 
            })

        except Exception as e:
            logger.error(f"Unexpected error: {str(e)}", exc_info=True)
            return Response(
                {'status': 'error', 'message': 'failed chatBot services', 'devMsg': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    
    
    def chat_bot_grok(self, request):
        try:
            import pdb;
            pdb.set_trace()
            
            payload = request.data
            user_message = payload.get('message')
            if not user_message:
                raise ValueError('Message is required.')

            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            }

            # prompt = f"""You are a financial advisor. A user says:
            # \"{user_message}\"
            # Provide personalized financial advice in simple terms."""
            
            prompt = user_message
            
            
            groq_payload = {
                "model": "llama-3.3-70b-versatile",  # Adjust model name if needed
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 600
            }

            response = requests.post(
                'https://api.groq.com/openai/v1/chat/completions',
                headers=headers,
                json=groq_payload,
                timeout=30
            )

            if response.status_code != 200:
                raise Exception(f"Groq API error: {response.text}")

            groq_response = response.json()

            return Response({
                'status': 'success',
                'response': groq_response['choices'][0]['message']['content'].strip()
            })

        except Exception as e:
            logger.error(f"Groq chatbot error: {str(e)}", exc_info=True)
            return Response(
                {'status': 'error', 'message': 'Groq chatbot failed', 'devMsg': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    # def chat_bot_grok(self, request):
    #     try:
            
    #         payload = request.data
    #         user_message = payload.get('message')
    #         conversation_id = payload.get('conversation_id')
    #         if not user_message:
    #             raise ValueError('Message is required.')

    #         # Call Dify API
    #         headers = {
    #             'Authorization': 'Bearer app-KQNmZMPxVgS1RVZLTfMrNp7n',  # Replace with your actual API key
    #             'Content-Type': 'application/json',
    #         }
            
        
    #         dify_payload={
    #         "query": user_message,
    #         "inputs": {},
    #         "response_mode": "blocking",
    #         "user": "user-001",
    #         "conversation_id": conversation_id if conversation_id else ""
    #         }

    #         response = requests.post(
    #             'https://api.dify.ai/v1/chat-messages',
    #             headers=headers,
    #             json=dify_payload
    #         )

    #         if response.status_code != 200:
    #             raise Exception(f"Dify API error: {response.text}")

    #         dify_response = response.json()

    #         return Response({
    #             'status': 'success',
    #             'response': dify_response.get('answer', 'No answer received'),  # adapt based on actual structure
    #             'conversation_id': dify_response.get('conversation_id', 'no conversation_id'), 
    #         })

    #     except Exception as e:
    #         logger.error(f"Unexpected error: {str(e)}", exc_info=True)
    #         return Response(
    #             {'status': 'error', 'message': 'failed chatBot services', 'devMsg': str(e)},
    #             status=status.HTTP_500_INTERNAL_SERVER_ERROR
    #         )
    