# Generated by Django 3.1.5 on 2021-01-15 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_auto_20210115_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotifytoken',
            name='expires_in',
            field=models.DateTimeField(),
        ),
    ]