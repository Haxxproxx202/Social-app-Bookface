# Generated by Django 4.0 on 2022-04-19 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sns', '0004_remove_extenduser_is_confirmed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extenduser',
            old_name='r',
            new_name='user',
        ),
    ]