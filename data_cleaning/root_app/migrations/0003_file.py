# Generated by Django 2.1.7 on 2019-03-22 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root_app', '0002_auto_20190309_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
