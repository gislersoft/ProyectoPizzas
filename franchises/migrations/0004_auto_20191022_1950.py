# Generated by Django 2.2.5 on 2019-10-23 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("franchises", "0003_auto_20191017_1910")]

    operations = [
        migrations.AlterModelOptions(name="plan", options={"ordering": ["price"]})
    ]