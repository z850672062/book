# Generated by Django 3.2.3 on 2021-05-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='gender',
            field=models.CharField(choices=[('M', '男性'), ('F', '女性')], default='M', max_length=2),
        ),
    ]
