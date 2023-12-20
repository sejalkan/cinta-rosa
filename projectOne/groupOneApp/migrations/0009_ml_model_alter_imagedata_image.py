# Generated by Django 4.2.7 on 2023-12-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("groupOneApp", "0008_merge_20231201_0936"),
    ]

    operations = [
        migrations.CreateModel(
            name="ML_Model",
            fields=[
                ("modelpath", models.FileField(upload_to="groupOneApp/ML_models")),
                ("ml_model_id", models.AutoField(primary_key=True, serialize=False)),
                ("accuracy", models.DecimalField(decimal_places=2, max_digits=4)),
                ("currentlyUsed", models.BooleanField(default=False)),
                ("snsheatmap", models.ImageField(upload_to="")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name="imagedata",
            name="image",
            field=models.ImageField(upload_to="groupOneApp/image_test"),
        ),
    ]
