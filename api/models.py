import re

import pytz
from django.db import models


# Create your models here.

def validate_payload(payload: str) -> str:
    """
    Function to valid Chat model payload to contain chars from ->
    *aA-zZ1234567890{}$%_-\\/~@#$%^&*()!?
    """
    if re.match('^[\w\s\D]+$', payload):
        return payload
    else:
        return "Text not valid"


class Timestamp(models.Model):
    """
    Model to store timestamp i.e when it was created and when
    it was updated
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Store(Timestamp):
    """Model for details of Store"""
    # get a tuple of all existing timezones to be used as a dropdown option
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    name = models.CharField(max_length=250, unique=True)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC', )
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Stores"
        ordering = ('name',)

    def __str__(self):
        return self.name


class Discount(Timestamp):
    """Model to store details for Discount"""
    store = models.ForeignKey(Store, related_name='discounts', on_delete=models.CASCADE)
    discount_code = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Discounts"

    def __str__(self):
        return self.discount_code


class Operator(Timestamp):
    """Model to store details for Operator"""
    operator_user = models.ForeignKey('auth.User', related_name='operators', on_delete=models.CASCADE)
    operator_group = models.CharField(max_length=250, unique=True)
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Operators"
        ordering = ('operator_group',)

    def __str__(self):
        return self.operator_user.get_full_name()


class Client(Timestamp):
    """Model to store Client details"""
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    client_user = models.ForeignKey('auth.User', related_name='clients', on_delete=models.CASCADE)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC', )
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name_plural = "Clients"
        ordering = ('timezone',)

    def __str__(self):
        return self.client_user.username


class Conversation(Timestamp):
    """Model to store details for a Conversation"""
    store = models.ForeignKey(Store, related_name='conversations', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='conversations', on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, related_name='conversations', on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Conversations"


class Chat(Timestamp):
    """Models to store details for  Chat"""
    conversation = models.ForeignKey(Conversation, related_name='chats', on_delete=models.CASCADE)
    payload = models.CharField(max_length=300, validators=[validate_payload])
    discount = models.ForeignKey(Discount, related_name='chats', on_delete=models.CASCADE)
    chat_user = models.ForeignKey('auth.User', related_name='chats', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='NEW')

    class Meta:
        verbose_name_plural = "Chats"
        ordering = ('-created',)

    def __str__(self):
        return self.payload


class Schedule(Timestamp):
    """Model to store a schedule. (used by celery)"""
    chat = models.ForeignKey(Chat, related_name='schedules', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Schedules"
