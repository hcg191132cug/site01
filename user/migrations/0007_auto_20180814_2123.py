# Generated by Django 2.0.3 on 2018-08-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20180814_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='service',
            field=models.ManyToManyField(related_name='companies_of', to='user.Service', verbose_name='服务项'),
        ),
    ]
