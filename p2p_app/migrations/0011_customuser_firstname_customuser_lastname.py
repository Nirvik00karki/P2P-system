# Generated by Django 5.0.4 on 2024-05-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2p_app', '0010_purchaseorder_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='firstname',
            field=models.TextField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='customuser',
            name='lastname',
            field=models.TextField(default='', max_length=255),
        ),
    ]
