# Generated by Django 4.2.3 on 2023-12-05 15:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("groupOneApp", "0013_alter_prediction_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prediction",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
