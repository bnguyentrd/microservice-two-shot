# Generated by Django 4.0.3 on 2022-12-03 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0004_rename_picture_url_shoes_pictured_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='binvo',
            name='import_href',
            field=models.CharField(default=1, max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
