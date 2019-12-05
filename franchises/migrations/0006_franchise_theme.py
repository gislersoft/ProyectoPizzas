# Generated by Django 2.2.5 on 2019-11-14 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("franchises", "0005_merge_20191107_1826")]

    operations = [
        migrations.AddField(
            model_name="franchise",
            name="theme",
            field=models.CharField(
                choices=[("#D32F2F", "well-red")],
                default="well-red",
                max_length=50,
                verbose_name="Tema",
            ),
        )
    ]
