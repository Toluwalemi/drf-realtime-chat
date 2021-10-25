# Generated by Django 3.2.8 on 2021-10-25 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_alter_chat_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='chat_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_chats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chat',
            name='conversation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversation_chats', to='api.conversation'),
        ),
        migrations.AlterField(
            model_name='chat',
            name='discount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discount_chats', to='api.discount'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_conversations', to='api.client'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='operator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operator_conversations', to='api.operator'),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_conversations', to='api.store'),
        ),
    ]
