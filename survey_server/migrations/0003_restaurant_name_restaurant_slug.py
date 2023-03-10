# Generated by Django 4.1.7 on 2023-03-02 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey_server', '0002_alter_restaurant_id_alter_survey_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='name',
            field=models.CharField(default='name', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(default='name', unique=True),
            preserve_default=False,
        ),
    ]
