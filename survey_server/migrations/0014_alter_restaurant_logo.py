# Generated by Django 4.1.7 on 2023-03-11 17:12

from django.db import migrations, models
import survey_server.models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_server', '0013_alter_restaurant_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='logo',
            field=models.ImageField(default=0, upload_to=survey_server.models.logo_upload_to),
        ),
    ]