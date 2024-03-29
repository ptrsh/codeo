# Generated by Django 3.1.4 on 2021-01-14 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=16, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Untitled', max_length=64)),
                ('language', models.CharField(max_length=20)),
                ('read', models.BooleanField(default=True)),
                ('read_link', models.CharField(max_length=4, null=True)),
                ('edit', models.BooleanField(default=False)),
                ('edit_link', models.CharField(max_length=6, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.author')),
            ],
        ),
    ]
