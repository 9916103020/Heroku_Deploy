# Generated by Django 3.1.2 on 2021-03-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0026_auto_20210306_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='extra_include',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]