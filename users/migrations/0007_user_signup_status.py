# Generated by Django 5.1.1 on 2024-10-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='signup_status',
            field=models.BooleanField(default=False),
        ),
    ]
