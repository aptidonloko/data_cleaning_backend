# Generated by Django 2.1.7 on 2019-03-23 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('root_app', '0004_auto_20190323_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='way',
            new_name='street',
        ),
    ]