# Generated by Django 2.2 on 2020-09-12 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0012_auto_20200912_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='dest1_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest1_price',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest2_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest2_price',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest3_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest3_price',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest4_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest4_price',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest5_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest5_price',
            field=models.PositiveIntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest6_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='destination',
            name='dest6_price',
            field=models.PositiveIntegerField(default='0'),
        ),
    ]
