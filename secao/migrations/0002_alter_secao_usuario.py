# Generated by Django 4.0.2 on 2022-04-04 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('secao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secao',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='usuario.usuario'),
        ),
    ]
