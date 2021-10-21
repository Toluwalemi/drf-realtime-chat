from django.urls import path

from .views import ApiRoot, ChatList, ChatDetail, ConversationList, ConversationDetail

# app_name = 'v1'

urlpatterns = [
    path('chats/', ChatList.as_view(), name=ChatList.name),
    path('chats/<int:pk>/', ChatDetail.as_view(), name=ChatDetail.name),
    path('conversations/', ConversationList.as_view(), name=ConversationList.name),
    path('conversations/<int:pk>/', ConversationDetail.as_view(), name=ConversationDetail.name),
    path('', ApiRoot.as_view(), name=ApiRoot.name),

]
