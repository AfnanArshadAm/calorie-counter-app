# Generated by Django 4.1.6 on 2023-02-01 03:07

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=60, null=True, verbose_name="email"
                    ),
                ),
                ("username", models.CharField(max_length=15, unique=True)),
                ("is_admin", models.BooleanField(blank=True, default=False, null=True)),
                ("is_staff", models.BooleanField(blank=True, default=False, null=True)),
                (
                    "is_superuser",
                    models.BooleanField(blank=True, default=False, null=True),
                ),
                ("is_active", models.BooleanField(blank=True, default=True, null=True)),
                ("full_name", models.TextField(blank=True, null=True)),
                ("phone", models.CharField(max_length=10)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
