# Generated by Django 5.2.1 on 2025-05-18 20:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(blank=True, unique=True)),
                (
                    "service_type",
                    models.CharField(
                        choices=[
                            ("WEBSITE", "Criação de Sites"),
                            ("CHATBOT", "Chatbots com IA"),
                            ("APP", "Aplicações sob Demanda"),
                        ],
                        max_length=20,
                    ),
                ),
                ("short_description", models.TextField()),
                ("description", models.TextField()),
                (
                    "features",
                    models.TextField(help_text="Digite cada recurso em uma nova linha"),
                ),
                (
                    "price_from",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("ACTIVE", "Ativo"), ("INACTIVE", "Inativo")],
                        default="ACTIVE",
                        max_length=20,
                    ),
                ),
                ("is_featured", models.BooleanField(default=False)),
                (
                    "whatsapp_message",
                    models.TextField(
                        default="Olá! Gostaria de saber mais sobre o serviço de {service_name}.",
                        help_text="Mensagem predefinida para o WhatsApp",
                    ),
                ),
                (
                    "whatsapp_number",
                    models.CharField(
                        help_text="Número do WhatsApp com código do país (ex: 5511999999999)",
                        max_length=20,
                    ),
                ),
                (
                    "featured_image",
                    models.ImageField(
                        blank=True,
                        help_text="Imagem principal do serviço",
                        null=True,
                        upload_to="services/featured/",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="ServiceFAQ",
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
                ("question", models.CharField(max_length=200)),
                ("answer", models.TextField()),
                ("order", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="faqs",
                        to="services.service",
                    ),
                ),
            ],
            options={
                "ordering": ["order", "created_at"],
            },
        ),
        migrations.CreateModel(
            name="ServiceProject",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        help_text="Imagem do projeto", upload_to="services/projects/"
                    ),
                ),
                ("url", models.URLField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="projects",
                        to="services.service",
                    ),
                ),
            ],
        ),
    ]
