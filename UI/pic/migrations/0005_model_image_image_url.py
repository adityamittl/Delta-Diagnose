# Generated by Django 3.1.3 on 2021-08-30 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pic', '0004_model_image_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_image',
            name='image_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
