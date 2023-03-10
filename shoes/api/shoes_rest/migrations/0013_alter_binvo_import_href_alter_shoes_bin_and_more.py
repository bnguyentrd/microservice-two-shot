# Generated by Django 4.0.3 on 2022-12-04 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0012_rename_picture_shoes_pictured_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='binvo',
            name='import_href',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='bin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='shoes', to='shoes_rest.binvo'),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='pictured_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
