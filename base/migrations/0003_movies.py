# Generated by Django 3.2.12 on 2024-02-16 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_universe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('watching_link', models.URLField()),
                ('universe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='base.universe')),
            ],
        ),
    ]