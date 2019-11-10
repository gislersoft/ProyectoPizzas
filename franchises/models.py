from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django_tenants.models import DomainMixin, TenantMixin
from django_tenants.postgresql_backend.base import _is_valid_schema_name

from simple_history.models import HistoricalRecords
from django.conf import settings

from users.models import User


class Module(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def initial_modules():
        Module.objects.get_or_create(name="Usuarios")
        Module.objects.get_or_create(name="Pizzas")

    def __str__(self):
        return self.name


class Plan(models.Model):
    @staticmethod
    def search(id):
        try:
            return Franchise.objects.get(id=id)
        except Franchise.DoesNotExist:
            return None



    name = models.CharField(max_length=100, verbose_name="nombre")
    description = models.CharField(
        max_length=1000, verbose_name="descripción", blank=True, null=True
    )
    price = models.PositiveIntegerField(verbose_name="precio")
    modules = models.ManyToManyField(Module, verbose_name="modulos")
    max_users = models.PositiveIntegerField(verbose_name="máximo de usuarios")

    class Meta:
        ordering = ["price"]

    def __str__(self):
        return self.name

    @staticmethod
    def search(id):
        try:
            return Plan.objects.get(id=id)
        except Plan.DoesNotExist:
            return None

    def get_avalaible_modules(self):
        return [str(module) for module in self.modules.all()]


def check_schema_name(name):
    if not _is_valid_schema_name(name):
        raise ValidationError("El nombre del esquema es inválido.")


class Franchise(TenantMixin):
    name = models.CharField("Nombre de la franquicia", max_length=300, unique=True)
    schema_name = models.CharField("Subdominio",
        max_length=300, unique=True, validators=[check_schema_name]
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Cliente de la franquicia",
        related_name="franchises",
        on_delete=models.SET_NULL,
        null=True,
    )
    plan = models.ForeignKey(
        Plan, related_name="franchises", on_delete=models.SET_NULL, null=True,
            verbose_name="Plan"
    )
    validity = models.DateTimeField("Fecha de vencimiento del servicio",
        help_text="Fecha hasta la que se encuentra pago el servicio"
    )

    def __str__(self):
        return self.name

    @classmethod
    def initial_franchise(cls):
        client = User.initial_user()
        Module.initial_modules()
        if not Franchise.objects.count():
            franchise = Franchise.objects.create(
                name="public", schema_name="public", validity="2099-12-31"
            )
            dominio = Domain.objects.create(
                tenant=franchise, is_primary=True, domain=settings.DOMAIN
            )

            print("Franquicia inicial creada correctamente")
        else:
            print("Ya existe una franquicia")

    def is_available(self):
        return self.validity >= timezone.now()

    @staticmethod
    def search(id):
        try:
            return Franchise.objects.get(id=id)
        except Franchise.DoesNotExist:
            return None

class Domain(DomainMixin):
    history = HistoricalRecords()

    def __str__(self):
        return self.domain
