# Generated by Django 4.1.7 on 2023-03-10 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_server', '0008_survey_customer_service_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='max_customer_service_score',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='max_food_quality_score',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='max_hygiene_score',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='max_menu_variety_score',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='max_value_for_money_score',
        ),
    ]
