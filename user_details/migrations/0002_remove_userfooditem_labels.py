# Generated by Django 4.1.6 on 2023-02-02 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_details", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userfooditem",
            name="labels",
        ),
    ]
