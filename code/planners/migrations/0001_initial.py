# Generated by Django 5.0.7 on 2024-09-21 16:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_id', models.IntegerField()),
                ('content_title', models.CharField(max_length=150)),
                ('custom_name', models.CharField(blank=True, max_length=150, null=True)),
                ('gpsX', models.DecimalField(decimal_places=7, max_digits=10)),
                ('gpsY', models.DecimalField(decimal_places=7, max_digits=10)),
                ('visit_date', models.DateField()),
                ('visit_time', models.TimeField()),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planners.plan')),
            ],
        ),
    ]
