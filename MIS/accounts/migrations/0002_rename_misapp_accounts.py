# Generated by Django 3.2.5 on 2021-07-31 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='misapp',
            new_name='accounts',
        ),
    ]