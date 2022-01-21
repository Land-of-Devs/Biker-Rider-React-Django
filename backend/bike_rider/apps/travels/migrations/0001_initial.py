# Generated by Django 3.0.2 on 2022-01-21 10:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bikes', '0001_initial'),
        ('bstations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('finish', models.DateTimeField()),
                ('bike', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bikes.Bike')),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='destination', to='bstations.BStation')),
                ('origin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='origin', to='bstations.BStation')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
