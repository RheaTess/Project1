# Generated by Django 4.2.5 on 2023-11-13 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='UserName',
            new_name='Name',
        ),
    ]
