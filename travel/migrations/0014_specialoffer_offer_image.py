# Generated by Django 2.2 on 2020-09-12 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_auto_20200912_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialoffer',
            name='offer_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]