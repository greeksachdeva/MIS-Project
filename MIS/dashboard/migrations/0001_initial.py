# Generated by Django 3.2.5 on 2021-08-08 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rolesall',
            fields=[
                ('first_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('roles', models.IntegerField(choices=[('0', 'Student'), ('1', 'Teacher')], max_length=1)),
            ],
        ),
    ]