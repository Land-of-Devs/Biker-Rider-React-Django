# Generated by Django 3.0.2 on 2022-01-26 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('min_minutes', models.IntegerField()),
                ('cent_minute', models.IntegerField()),
            ],
        ),
    ]
