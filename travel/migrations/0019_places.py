# Generated by Django 2.2 on 2020-09-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0018_heading_main_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip', models.CharField(max_length=200)),
                ('day1_place', models.CharField(max_length=2000)),
                ('day2_place', models.CharField(max_length=2000)),
                ('day3_place', models.CharField(max_length=2000)),
                ('day4_place', models.CharField(max_length=2000)),
                ('day1_text', models.CharField(max_length=2000)),
                ('day2_text', models.CharField(max_length=2000)),
                ('day3_text', models.CharField(max_length=2000)),
                ('day4_text', models.CharField(max_length=2000)),
                ('day1_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('day2_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('day3_image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('day4_image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]