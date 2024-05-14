# Generated by Django 3.2.12 on 2024-05-01 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0012_auto_20240222_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universe',
            name='genres',
            field=models.ManyToManyField(related_name='universes', to='base.Genre'),
        ),
        migrations.AlterField(
            model_name='universe',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participating_universes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_accounts', models.TextField(blank=True, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('interests', models.ManyToManyField(related_name='interested_users', to='base.Genre')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
