# Generated by Django 2.2.17 on 2021-01-13 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210112_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.User'),
        ),
        migrations.AddField(
            model_name='sales_order',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.User'),
        ),
        migrations.AddField(
            model_name='spoilage',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.User'),
        ),
        migrations.AddField(
            model_name='transfer',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.User'),
        ),
        migrations.AlterField(
            model_name='purchase_order',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Vendor'),
        ),
        migrations.AlterField(
            model_name='sales_order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Customer'),
        ),
    ]
