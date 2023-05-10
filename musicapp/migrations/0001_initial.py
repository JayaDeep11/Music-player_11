# Generated by Django 3.0.6 on 2022-07-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('song_img', models.FileField(upload_to='')),
                ('year', models.IntegerField()),
                ('singer', models.CharField(max_length=200)),
                ('song_file', models.FileField(upload_to='')),
            ],
        ),
    ]
