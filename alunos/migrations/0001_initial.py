# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricula', models.CharField(max_length=20)),
                ('Ano_letivo', models.IntegerField()),
                ('Faltas', models.FloatField()),
                ('Media_Final', models.FloatField()),
                ('Frequencia', models.FloatField()),
                ('Sexo', models.CharField(max_length=1)),
                ('Renda', models.FloatField()),
                ('Tipo_Escola_Origem', models.CharField(max_length=100)),
                ('Etnia', models.CharField(max_length=20)),
                ('Reside', models.CharField(max_length=100)),
                ('CoefRendimento', models.FloatField()),
                ('AcessoBiblioteca', models.FloatField()),
                ('ETEP', models.FloatField()),
                ('Projeto', models.FloatField()),
                ('BolsaEstudo', models.FloatField()),
                ('Situacao', models.CharField(max_length=20)),
            ],
        ),
    ]
