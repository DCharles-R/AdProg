# Generated by Django 5.1.3 on 2024-12-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('valor', models.FloatField()),
                ('ubicacion', models.CharField()),
            ],
        ),
    ]