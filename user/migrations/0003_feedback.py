# Generated by Django 4.2.5 on 2023-11-13 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_username_register_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('PhNo', models.IntegerField()),
                ('Message', models.CharField(max_length=30)),
            ],
        ),
    ]
