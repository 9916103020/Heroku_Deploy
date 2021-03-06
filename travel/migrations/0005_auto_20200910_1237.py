# Generated by Django 2.2 on 2020-09-10 07:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20200910_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('heading_text', models.CharField(max_length=50)),
                ('dest1', models.CharField(max_length=50)),
                ('dest1_price', models.PositiveIntegerField()),
                ('dest1_days', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest1_nights', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest1_accomodation', models.CharField(max_length=10)),
                ('dest1_transportation', models.CharField(max_length=10)),
                ('dest1_food', models.CharField(max_length=10)),
                ('dest1_star', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest1_reviewcount', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest2', models.CharField(max_length=50)),
                ('dest2_price', models.PositiveIntegerField()),
                ('dest2_days', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest2_nights', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest2_accomodation', models.CharField(max_length=10)),
                ('dest2_transportation', models.CharField(max_length=10)),
                ('dest2_food', models.CharField(max_length=10)),
                ('dest2_star', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest2_reviewcount', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest3', models.CharField(max_length=50)),
                ('dest3_price', models.PositiveIntegerField()),
                ('dest3_days', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest3_nights', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest3_accomodation', models.CharField(max_length=10)),
                ('dest3_transportation', models.CharField(max_length=10)),
                ('dest3_food', models.CharField(max_length=10)),
                ('dest3_star', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest3_reviewcount', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest4', models.CharField(max_length=50)),
                ('dest4_price', models.PositiveIntegerField()),
                ('dest4_days', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest4_nights', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest4_accomodation', models.CharField(max_length=10)),
                ('dest4_transportation', models.CharField(max_length=10)),
                ('dest4_food', models.CharField(max_length=10)),
                ('dest4_star', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest4_reviewcount', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest5', models.CharField(max_length=50)),
                ('dest5_price', models.PositiveIntegerField()),
                ('dest5_days', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest5_nights', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest5_accomodation', models.CharField(max_length=10)),
                ('dest5_transportation', models.CharField(max_length=10)),
                ('dest5_food', models.CharField(max_length=10)),
                ('dest5_star', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest5_reviewcount', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest6', models.CharField(max_length=50)),
                ('dest6_price', models.PositiveIntegerField()),
                ('dest6_days', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest6_nights', models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest6_accomodation', models.CharField(max_length=10)),
                ('dest6_transportation', models.CharField(max_length=10)),
                ('dest6_food', models.CharField(max_length=10)),
                ('dest6_star', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('dest6_reviewcount', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
            ],
        ),
        migrations.RemoveField(
            model_name='footer',
            name='dest1',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='dest2',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='dest3',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='dest4',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='dest5',
        ),
    ]
