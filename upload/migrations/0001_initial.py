# Generated by Django 4.0.2 on 2022-03-23 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FileField(upload_to='uploads/')),
                ('nome', models.TextField(max_length=100)),
                ('extensao', models.TextField(max_length=10)),
                ('tipo_arquivo', models.CharField(max_length=100)),
                ('data', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]