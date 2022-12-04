# Generated by Django 4.0.3 on 2022-12-04 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0010_alter_binvo_import_href'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoes',
            old_name='pictured_url',
            new_name='picture',
        ),
        migrations.AlterField(
            model_name='shoes',
            name='bin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='shoes_rest.binvo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoes',
            name='color',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='manufacturer',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='model_name',
            field=models.CharField(max_length=250),
        ),
    ]
