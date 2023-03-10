# Generated by Django 4.1.7 on 2023-03-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_server', '0014_alter_restaurant_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('starter', 'Starter'), ('main', 'Main'), ('dessert', 'Dessert'), ('drink', 'Drink')], max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
