# Generated by Django 4.2.5 on 2023-12-01 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_delete_servicedate_bookingform_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingform',
            name='Status',
            field=models.IntegerField(default=0),
        ),
    ]
