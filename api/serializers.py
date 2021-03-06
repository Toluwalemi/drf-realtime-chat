from rest_framework import serializers

from api.models import Store, Discount, Operator, Client, Conversation, Chat, Schedule


class StoreSerializer(serializers.ModelSerializer):
    timezone = serializers.ChoiceField(choices=Store.TIMEZONES)
    timezone_description = serializers.CharField(
        source='get_timezone_display',
        read_only=True
    )

    class Meta:
        model = Store
        fields = ('pk', 'name', 'timezone',
                  'timezone_description', 'phone_number')


class DiscountSerializer(serializers.ModelSerializer):
    store = StoreSerializer()

    class Meta:
        model = Discount
        fields = ('pk', 'discount_code', 'store')


class OperatorSerializer(serializers.ModelSerializer):
    operator_user = serializers.ReadOnlyField(source='operator_user.username')

    class Meta:
        model = Operator
        fields = ('pk', 'operator_user', 'operator_group', 'phone_number')


class ClientSerializer(serializers.ModelSerializer):
    timezone = serializers.ChoiceField(choices=Store.TIMEZONES)
    timezone_description = serializers.CharField(
        source='get_timezone_display',
        read_only=True
    )
    client_user = serializers.ReadOnlyField(source='client_user.username')

    class Meta:
        model = Client
        fields = ('pk', 'client_user', 'timezone', 'timezone_description', 'phone_number')


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    discount = DiscountSerializer()
    user_id = serializers.ReadOnlyField(source='chat_user.pk')

    class Meta:
        model = Chat
        fields = ('url', 'id', 'payload', 'user_id', 'created', 'discount', 'status',)
        read_only_fields = ('status',)


class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    chats = ChatSerializer(many=True, read_only=True, source='conversation_chats')
    store_id = serializers.SlugRelatedField(queryset=Store.objects.all(), slug_field='pk', source='store')
    client_id = serializers.SlugRelatedField(queryset=Client.objects.all(), slug_field='pk', source='client')
    operator_id = serializers.SlugRelatedField(queryset=Operator.objects.all(), slug_field='pk', source='operator')

    class Meta:
        model = Conversation
        fields = ('url', 'store_id', 'operator_id', 'client_id', 'status', 'chats',)


class ChatConversationSerializer(serializers.ModelSerializer):
    conversation_id = serializers.SlugRelatedField(queryset=Conversation.objects.all(), slug_field='pk',
                                                   source='conversation')

    discount_id = serializers.SlugRelatedField(queryset=Discount.objects.all(), slug_field='discount_code',
                                               write_only=True, source='discount')

    class Meta:
        model = Chat
        fields = ('id', 'payload', 'user_id', 'discount_id', 'conversation_id', 'created', 'status',)
        read_only_fields = ('status', 'id',)


class ScheduleSerializer(serializers.ModelSerializer):
    chat = ChatConversationSerializer()

    class Meta:
        model = Schedule
        fields = ('chat',)
