# Generated by Django 2.2.6 on 2021-01-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210105_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
