# Generated by Django 3.2.8 on 2021-10-20 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ('timezone',), 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='conversation',
            options={'verbose_name_plural': 'Conversations'},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name_plural': 'Schedules'},
        ),
    ]
