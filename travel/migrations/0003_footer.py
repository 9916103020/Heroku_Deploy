# Generated by Django 2.2 on 2020-09-10 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_navbar'),
    ]

    operations = [
        migrations.CreateModel(
            name='footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=50)),
                ('link_text', models.CharField(max_length=50)),
                ('popular_text', models.CharField(max_length=50)),
                ('dest1', models.CharField(max_length=50)),
                ('dest2', models.CharField(max_length=50)),
                ('dest3', models.CharField(max_length=50)),
                ('dest4', models.CharField(max_length=50)),
                ('dest5', models.CharField(max_length=50)),
                ('contact_text', models.CharField(max_length=50)),
                ('phonecode', models.IntegerField(max_length=3)),
                ('phonenumber', models.IntegerField(max_length=10)),
                ('emailid', models.EmailField(max_length=254)),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
            ],
        ),
    ]
