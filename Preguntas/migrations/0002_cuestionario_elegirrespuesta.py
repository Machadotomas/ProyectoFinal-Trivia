# Generated by Django 3.2.6 on 2021-08-28 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Preguntas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cuestionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='ingresa la pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='ElegirRespuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='esta es la correcta?')),
                ('texto', models.TextField(verbose_name='ingrese las respuestas aqui')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preguntas', to='Preguntas.cuestionario')),
            ],
        ),
    ]
