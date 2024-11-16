from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatbotRequestSerializer
from .utils import get_chat_response

class ChatbotAPIView(APIView):

    def post(self, request):
        serializer = ChatbotRequestSerializer(data=request.data)
        if serializer.is_valid():
            user_message = serializer.validated_data['message']

            try:
                chatbot_response = get_chat_response(user_message)
                return Response({"message": chatbot_response}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
