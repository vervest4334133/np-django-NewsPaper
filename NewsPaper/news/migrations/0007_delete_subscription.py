# Generated by Django 5.0 on 2024-01-09 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_subscription'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
