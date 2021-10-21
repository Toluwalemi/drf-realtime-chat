from rest_framework import serializers

from api.models import Store, Discount, Operator, Client, Conversation, Chat


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    discounts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True
    )
    timezone = serializers.ChoiceField(choices=Store.TIMEZONES)
    timezone_description = serializers.CharField(
        source='get_timezone_display',
        read_only=True
    )

    class Meta:
        model = Store
        fields = ('url', 'pk', 'name', 'timezone',
                  'timezone_description', 'phone_number')


class DiscountSerializer(serializers.HyperlinkedModelSerializer):
    store = serializers.SlugRelatedField(
        queryset=Store.objects.all(),
        slug_field='name')

    class Meta:
        model = Discount
        fields = ('url', 'pk', 'discount_code', 'store')


class OperatorSerializer(serializers.HyperlinkedModelSerializer):
    operator_user = serializers.ReadOnlyField(source='operator_user.username')

    class Meta:
        model = Operator
        fields = ('url', 'pk', 'operator_name', 'operator_group', 'phone_number')


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    timezone = serializers.ChoiceField(choices=Store.TIMEZONES)
    timezone_description = serializers.CharField(
        source='get_timezone_display',
        read_only=True
    )
    client_user = serializers.ReadOnlyField(source='client_user.username')

    class Meta:
        model = Client
        fields = ('url', 'pk', 'timezone', 'timezone_description', 'phone_number')


class ChatSerializer(serializers.HyperlinkedModelSerializer):
    discount = DiscountSerializer()

    class Meta:
        model = Chat
        fields = ('url', 'pk', 'payload', 'status', 'created', 'discount')


class ConversationSerializer(serializers.HyperlinkedModelSerializer):
    chats = ChatSerializer(many=True, read_only=True)
    store = StoreSerializer()
    client = ClientSerializer()
    operator = OperatorSerializer()

    class Meta:
        model = Conversation
        fields = ('url', 'pk', 'status', 'store', 'client', 'operator', 'chats')


class ChatConversationSerializer(serializers.ModelSerializer):
    conversation = serializers.SlugRelatedField(queryset=Conversation.objects.all(), slug_field='name')
    discount = serializers.SlugRelatedField(queryset=Discount.objects.all(), slug_field='name')

    class Meta:
        model = Chat
        fields = ('url', 'pk', 'payload', 'status', 'created', 'conversation', 'discount')
