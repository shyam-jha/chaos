# Generated by Django 3.2.12 on 2024-02-20 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_universe_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='gross_income',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
