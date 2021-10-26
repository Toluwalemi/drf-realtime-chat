# Create your views here.
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView, \
    ListAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.models import Conversation, Chat, Schedule
from api.serializers import ChatConversationSerializer, ConversationSerializer, StoreSerializer, ScheduleSerializer


class ConversationList(ListCreateAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    name = 'conversation-list'


class ConversationDetail(RetrieveUpdateDestroyAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    name = 'conversation-detail'


class ChatCreate(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatConversationSerializer
    name = 'chat-create'


class ChatList(ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    name = 'chat-list'


class ChatDetail(RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatConversationSerializer
    name = 'chat-detail'


class ApiRoot(GenericAPIView):
    name = 'api-root'
    serializer_class = StoreSerializer

    def get(self, request, *args, **kwargs):
        return Response({
            'chats': reverse(ChatList.name, request=request),
            'create-chat': reverse(ChatCreate.name, request=request),
            'conversations': reverse(ConversationList.name, request=request),
        })
