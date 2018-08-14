# Generated by Django 2.0.3 on 2018-08-02 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('pub_time', models.DateTimeField(auto_now_add=True, verbose_name=False)),
                ('update_time', models.DateTimeField(verbose_name=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(default='未知', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='blogs', to='user.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='分类')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='随机留言者')),
                ('head_img', models.ImageField(upload_to='comment_user')),
                ('comment_time', models.DateTimeField(auto_now_add=True, verbose_name=False)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='blog.Category'),
        ),
    ]
