# Generated by Django 2.2.17 on 2021-01-12 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210112_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spoilage',
            old_name='total_amount_due',
            new_name='total_lost',
        ),
    ]
