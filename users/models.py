import os

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.utils.functional import cached_property


def avatar_path(instance, filename):
    _, file_extension = os.path.splitext(filename)

    return "/".join(["users", str(instance.id), f"avatar{file_extension}"])


class customManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name):
        user = User.objects.create(
            email=email, first_name=first_name, last_name=last_name, is_active=True
        )
        user.set_password(password)
        user.save()

    def create_superuser(self, email, password, first_name, last_name):
        user = User.objects.create(
            email=email, first_name=first_name, last_name=last_name, is_active=True
        )
        user.set_password(password)
        user.save()


class User(AbstractBaseUser):
    objects = customManager()

    ADMINISTRATOR = "Administrador"
    DIGITIZER = "Digitador"
    FRANCHISE = "Franquicia"
    CLIENT = "Cliente"
    USER_TYPES = (
        (ADMINISTRATOR, ADMINISTRATOR),
        (DIGITIZER, DIGITIZER),
        (FRANCHISE, FRANCHISE),
        (CLIENT, CLIENT),
    )
    DEFAULT_AVATAR = "images/profile.png"

    email = models.EmailField("Correo Electrónico", blank=True, unique=True)
    first_name = models.CharField("Nombres", max_length=150, blank=True)
    last_name = models.CharField("Apellidos", max_length=150, blank=True)

    is_staff = models.BooleanField("Staff?", default=False)
    is_active = models.BooleanField("Activo?", default=True)
    date_joined = models.DateTimeField(auto_now_add=True, auto_now=False)
    avatar = models.ImageField(
        verbose_name="Imagen", upload_to=avatar_path, blank=True, null=True
    )
    user_type = models.CharField(
        "Tipo de Usuario",
        max_length=50,
        choices=USER_TYPES,
        null=False,
        blank=True,
        default=USER_TYPES[2][0],
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return f"{settings.STATIC_URL}{User.DEFAULT_AVATAR}"

    @classmethod
    def initial_user(
        cls, email="admin@admin.co", password="superpizzas", hash_password=None
    ):
        if not User.objects.count():
            user = User.objects.create(
                email=email, is_active=True, user_type=User.ADMINISTRATOR
            )
            if hash_password:
                user.password = hash_password
            else:
                user.set_password(password)
            user.save()
            return User

        return User.objects.get(email=email)
