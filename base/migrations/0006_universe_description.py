# Generated by Django 3.2.12 on 2024-02-16 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='universe',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
