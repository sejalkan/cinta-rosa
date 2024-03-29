# Generated by Django 4.2.7 on 2023-11-28 13:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("groupOneApp", "0002_alter_prediction_image_delete_userimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imagedata",
            name="classification",
            field=models.IntegerField(
                choices=[(0, "normal"), (1, "benign"), (2, "malignant")]
            ),
        ),
        migrations.AlterField(
            model_name="imagedata",
            name="image",
            field=models.ImageField(upload_to="projectOne/groupOneApp/static"),
        ),
        migrations.AlterField(
            model_name="imagedata",
            name="set",
            field=models.IntegerField(
                choices=[(0, "test"), (1, "train"), (2, "validation")]
            ),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="result",
            field=models.IntegerField(choices=[(0, "low"), (1, "medium"), (2, "high")]),
        ),
        migrations.AlterField(
            model_name="prediction",
            name="timestamp",
            field=models.IntegerField(
                choices=[(0, "beforePrediction"), (1, "afterPrediction")]
            ),
        ),
    ]
