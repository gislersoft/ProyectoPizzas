# Generated by Django 2.2.5 on 2019-09-26 22:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pizzas.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Topping",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, verbose_name="Nombre")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=pizzas.models.topping_image_path,
                        verbose_name="Imagen",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Pizza",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=pizzas.models.pizza_image_path,
                        verbose_name="Imagen",
                    ),
                ),
                ("price", models.FloatField(verbose_name="Precio")),
                (
                    "toppings",
                    models.ManyToManyField(related_name="pizzas", to="pizzas.Topping"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Pendiente", "Pendiente"),
                            ("Pagada", "Pagada"),
                            ("Cancelada", "Cancelada"),
                        ],
                        max_length=50,
                        verbose_name="Estado",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "pizzas",
                    models.ManyToManyField(related_name="orders", to="pizzas.Pizza"),
                ),
            ],
        ),
    ]
