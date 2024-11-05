from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils.llm_client import get_response_from_llm

from .models import Message
from .serializers import MessageSerializer

@api_view(['POST'])
def chat_view(request):
    message = request.data.get("message")

    response = get_response_from_llm(message)
    
    return Response({"response": response})

@api_view(['GET'])
def get_all_chats(request):
    messages = Message.objects.all()

    serializer = MessageSerializer(messages, many=True)
    return Response(serializer)