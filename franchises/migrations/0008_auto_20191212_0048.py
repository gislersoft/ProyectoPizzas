# Generated by Django 2.2.8 on 2019-12-12 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('franchises', '0007_auto_20191124_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='franchise',
            name='color',
            field=models.CharField(choices=[('coffee', 'Café'), ('dark', 'Oscuro'), ('dust', 'Arena'), ('gray', 'Gris'), ('lime', 'Lima'), ('mint', 'Menta'), ('navy', 'Azul marino'), ('ocean', 'Oceano'), ('prickly-pear', 'Higo'), ('purple', 'Violeta'), ('well-red', 'Rojo'), ('yellow', 'Amarillo')], default='well-red', max_length=50, verbose_name='Tema'),
        ),
    ]
