# Generated by Django 3.1.2 on 2021-03-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0027_offer_extra_include'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='highlight1',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='highlight2',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='highlight3',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='highlight4',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='highlight5',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]