# Generated by Django 5.0.7 on 2024-07-21 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.CharField(default=False, max_length=20),
            preserve_default=False,
        ),
    ]
