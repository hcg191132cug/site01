# Generated by Django 2.0.3 on 2018-08-02 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default='未知', max_length=30, verbose_name='公司名'),
        ),
    ]
