# Generated by Django 3.1.1 on 2020-09-25 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=16)),
                ('password_hash', models.CharField(max_length=16)),
                ('r_link', models.CharField(max_length=8)),
                ('rw_link', models.CharField(max_length=8)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.author')),
            ],
        ),
    ]
