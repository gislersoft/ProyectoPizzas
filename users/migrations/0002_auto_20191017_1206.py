# Generated by Django 2.2.5 on 2019-10-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="user_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Administrador", "Administrador"),
                    ("Franquicia", "Franquicia"),
                    ("Cliente", "Cliente"),
                ],
                max_length=50,
                null=True,
                verbose_name="Tipo de Usuario",
            ),
        )
    ]
