# Generated by Django 4.1.7 on 2023-03-10 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey_server', '0009_remove_survey_max_customer_service_score_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voucher',
            old_name='vocher_code',
            new_name='voucher_code',
        ),
    ]
