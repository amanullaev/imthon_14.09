# Generated by Django 4.2.5 on 2023-09-14 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('field_api', '0002_remove_bookingmodel_date_bookingmodel_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingmodel',
            old_name='data',
            new_name='date',
        ),
    ]
