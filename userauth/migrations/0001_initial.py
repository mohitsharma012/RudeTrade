# Generated by Django 4.1.9 on 2023-05-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rudeusers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_pass', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('user_email', models.CharField(max_length=50)),
                ('currency', models.CharField(max_length=25)),
                ('country', models.CharField(max_length=25)),
            ],
        ),
    ]