# Generated by Django 3.1.1 on 2020-09-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200928_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='password_hash',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]