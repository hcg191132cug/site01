# Generated by Django 2.0.3 on 2018-08-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180809_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
