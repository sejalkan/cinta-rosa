# Generated by Django 4.2.6 on 2023-12-08 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('groupOneApp', '0019_alter_ml_model_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='ml_model',
            name='train_accuracy',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ml_model',
            name='val_accuracy',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
    ]
