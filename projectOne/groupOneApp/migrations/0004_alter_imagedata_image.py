# Generated by Django 4.2.7 on 2023-11-28 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "groupOneApp",
            "0003_alter_imagedata_classification_alter_imagedata_image_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagedata",
            name="image",
            field=models.ImageField(upload_to="projectOne/image_test"),
        ),
    ]
