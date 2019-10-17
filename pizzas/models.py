import os

from django.conf import settings
from django.db import models


def topping_image_path(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return "/toppings/".join(["users", str(instance.id), f"image{file_extension}"])


class Topping(models.Model):
    DEFAULT_IMAGE = "images/topping_default.png"

    name = models.CharField("Nombre", max_length=250)
    image = models.ImageField(
        verbose_name="Imagen", upload_to=topping_image_path, blank=True, null=True
    )

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return f"{settings.STATIC_URL}{Topping.DEFAULT_IMAGE}"


def pizza_image_path(instance, filename):
    _, file_extension = os.path.splitext(filename)
    return "/".join(["pizzas", str(instance.id), f"image{file_extension}"])


class Pizza(models.Model):
    DEFAULT_IMAGE = "images/pizza_default.png"
    image = models.ImageField(
        verbose_name="Imagen", upload_to=pizza_image_path, blank=True, null=True
    )
    toppings = models.ManyToManyField(Topping, related_name="pizzas")
    price = models.FloatField(verbose_name="Precio")

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return f"{settings.STATIC_URL}{Pizza.DEFAULT_IMAGE}"


class Order(models.Model):
    STATE_PENDIENT = "Pendiente"
    STATE_PAID = "Pagada"
    STATE_CANCELED = "Cancelada"

    STATE_CHOICES = (
        (STATE_PENDIENT, STATE_PENDIENT),
        (STATE_PAID, STATE_PAID),
        (STATE_CANCELED, STATE_CANCELED),
    )

    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="orders",
        on_delete=models.SET_NULL,
        null=True,
    )
    pizzas = models.ManyToManyField(Pizza, related_name="orders")
    state = models.CharField("Estado", choices=STATE_CHOICES, max_length=50)
