# Generated by Django 2.2.6 on 2021-01-05 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210104_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase_order',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Vendor'),
        ),
    ]
