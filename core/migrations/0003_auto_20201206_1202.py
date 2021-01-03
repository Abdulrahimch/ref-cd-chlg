# Generated by Django 3.0.3 on 2020-12-06 12:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='TC',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='TC number must have 11 digits, should not start with Zero', regex='^[1-9]\\d{10}$')]),
        ),
    ]