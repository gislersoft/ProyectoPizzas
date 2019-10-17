from django.core.exceptions import ValidationError
from django.db import models
from django_tenants.models import DomainMixin, TenantMixin
from django_tenants.postgresql_backend.base import _is_valid_schema_name

from simple_history.models import HistoricalRecords
from django.conf import settings

from users.models import User


class Module(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def create_initial_modules():
        if Module.objects.all().count() == 0:
            Module.objects.create(name="Reportes")
            Module.objects.create(name="Temas")
            Module.objects.create(name="Usuarios")

    def __str__(self):
        return self.name
    def __str__(self):
        return self.name


class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    modules = models.ManyToManyField(Module)
    max_users = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    @staticmethod
    def search(id):
        try:
            return Plan.objects.get(id=id)
        except Plan.DoesNotExist:
            return None

    @staticmethod
    def create_init_plans():
        Module.create_initial_modules()
        if Plan.objects.all().count() == 0:
            plan = Plan.objects.create(name="Gratuito", price=0, max_users=5)
            plan.modulos_disponibles = Module.objects.filter(
                name__in=[
                    "Reportes",
                    "Temas",
                    "Usuarios",
                ]
            )
            plan.save()
            plan = Plan.objects.create(
                name="Estandar", price=25, max_users=100
            )
            plan.modulos_disponibles = Module.objects.filter(
                name__in=[
                    "Reportes",
                    "Temas",
                    "Usuarios",
                ]
            )
            plan.save()
            plan = Plan.objects.create(
                name="Empresarial", price=199, max_users=1000
            )
            plan.modulos_disponibles = Module.objects.filter(
                name__in=[
                    "Reportes",
                    "Temas",
                    "Usuarios",
                ]
            )
            plan.save()

    def get_avalaible_modules(self):
        return [str(module) for module in self.modules.all()]


def check_schema_name(name):
    if not _is_valid_schema_name(name):
        raise ValidationError("El name del esquema es inválido.")


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
        if not Franchise.objects.count():
            franchise = Franchise.objects.create(name="public",schema_name="public",validity="2099-12-31")
            dominio = Domain.objects.create(tenant=franchise, is_primary=True, domain=settings.DOMAIN)

            print("Franquicia inicial creata correctamente")
        else:
            print("Ya existe una franquicia")

class Domain(DomainMixin):
    history = HistoricalRecords()
