# Create your views here.
from django.http import JsonResponse
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView, \
    ListAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle

from api.models import Conversation, Chat, Schedule
from api.serializers import ChatConversationSerializer, ConversationSerializer, StoreSerializer, ScheduleSerializer


def ping(request):
    """Health Check"""
    data = {"ping": "pong!"}
    return JsonResponse(data)


class ConversationList(ListCreateAPIView):
    """Create a conversation and view all conversations"""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    name = 'conversation-list'


class ConversationDetail(RetrieveUpdateDestroyAPIView):
    """Retrieve, delete or update a conversation"""
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    name = 'conversation-detail'


class ChatCreate(CreateAPIView):
    """Create a chat. The throttle serves as rate limit. See settings.py"""
    throttle_scope = 'chats'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Chat.objects.all()
    serializer_class = ChatConversationSerializer
    name = 'chat-create'


class ChatList(ListAPIView):
    """View all sent chats as soon as celery does it job in tasks.py"""
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    name = 'chat-list'


class ChatDetail(RetrieveUpdateDestroyAPIView):
    """Retrieve update and delete a chat. Also uses rate limit 90/hour"""
    throttle_scope = 'chats'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Chat.objects.all()
    serializer_class = ChatConversationSerializer
    name = 'chat-detail'


class ApiRoot(GenericAPIView):
    """Helps with navigation when you go to the /api endpoint"""
    name = 'api-root'
    serializer_class = StoreSerializer

    def get(self, request, *args, **kwargs):
        return Response({
            'chats': reverse(ChatList.name, request=request),
            'create-chat': reverse(ChatCreate.name, request=request),
            'conversations': reverse(ConversationList.name, request=request),
        })
