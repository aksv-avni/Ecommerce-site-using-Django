# Generated by Django 4.0.6 on 2022-07-29 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='undefined', max_length=200),
            preserve_default=False,
        ),
    ]
