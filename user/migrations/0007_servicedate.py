# Generated by Django 4.2.5 on 2023-11-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_bookingform_email_remove_bookingform_phno_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
            ],
        ),
    ]
