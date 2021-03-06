# Generated by Django 2.2.17 on 2021-02-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_user_branch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='login',
        ),
        migrations.AddField(
            model_name='user',
            name='auth_level',
            field=models.CharField(default='Employee', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='top_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Login',
        ),
    ]
