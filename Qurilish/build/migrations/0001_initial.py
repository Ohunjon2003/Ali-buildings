# Generated by Django 5.0.3 on 2024-06-01 05:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Qurilish_tashkiloti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('when_organized_found', models.CharField(max_length=50, verbose_name='qachon_tashkil_topgan')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.area')),
            ],
        ),
        migrations.CreateModel(
            name='Qurilish_binosi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.CharField(blank=True, max_length=100, null=True, verbose_name='maydoni')),
                ('floor', models.IntegerField(default=0, verbose_name='qavat')),
                ('parking_lot', models.BooleanField(default=True, verbose_name='parkovka')),
                ('playground', models.BooleanField(verbose_name="o'yin maydonchasi")),
                ('lift', models.BooleanField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.area')),
                ('qurilish_tashkiloti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='build.qurilish_tashkiloti')),
            ],
        ),
    ]
