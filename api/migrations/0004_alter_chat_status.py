# Generated by Django 3.2.8 on 2021-10-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_discount_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='status',
            field=models.CharField(default='NEW', max_length=10),
        ),
    ]