# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.models import Conversation, Chat
from api.serializers import ChatConversationSerializer, ConversationSerializer, StoreSerializer


class ConversationList(generics.ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    name = 'conversation-list'


class ConversationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    name = 'conversation-detail'


class ChatList(generics.ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatConversationSerializer
    name = 'chat-list'


class ChatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatConversationSerializer
    name = 'chat-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    serializer_class = StoreSerializer

    def get(self, request, *args, **kwargs):
        return Response({
            'chats': reverse(ChatList.name, request=request),
            'conversations': reverse(ConversationList.name, request=request),
        })
