from django.core.exceptions import ValidationError
from django.db import models
from django_tenants.models import DomainMixin, TenantMixin
from django_tenants.postgresql_backend.base import _is_valid_schema_name

from django.conf import settings

from users.models import User


class Module(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def initual_modules():
        Module.objects.get_or_create(name="Usuarios")
        Module.objects.get_or_create(name="Pizzas")

    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    modules = models.ManyToManyField(Module)
    max_users = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def get_avalaible_modules(self):
        return [str(module) for module in self.modules.all()]


def check_schema_name(name):
    if not _is_valid_schema_name(name):
        raise ValidationError("El nombre del esquema es inválido.")


class Franchise(TenantMixin):
    name = models.CharField("Nombre de la franquicia", max_length=300, unique=True)
    schema_name = models.CharField(
        max_length=300, unique=True, validators=[check_schema_name]
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Cliente de la franquicia",
        related_name="franchises",
        on_delete=models.SET_NULL,
        null=True
    )
    plan = models.ForeignKey(Plan, related_name="franchises", on_delete=models.SET_NULL, null=True)
    validity = models.DateTimeField(
        help_text="Fecha hasta la que se encuentra pago el servicio"
    )

    def __str__(self):
        return self.name
    
    @classmethod
    def initial_franchise(cls):
        client = User.initial_user()
        Module.initual_modules()
        if not Franchise.objects.count():
            franchise = Franchise.objects.create(name="public",schema_name="public",validity="2099-12-31")
            dominio = Domain.objects.create(tenant=franchise, is_primary=True, domain=settings.DOMAIN)

            print("Franquicia inicial creata correctamente")
        else:
            print("Ya existe una franquicia")

class Domain(DomainMixin):
    pass
