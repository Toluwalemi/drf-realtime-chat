from django.contrib import admin

# Register your models here.
from api.models import Store, Discount, Operator, Client, Conversation, Chat, Schedule

admin.site.register(Store)
admin.site.register(Discount)
admin.site.register(Operator)
admin.site.register(Client)
admin.site.register(Conversation)
admin.site.register(Chat)
admin.site.register(Schedule)
