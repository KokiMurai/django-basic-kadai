# Generated by Django 5.1 on 2024-09-01 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crud", "0003_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="img",
            field=models.ImageField(blank=True, default="noImage.png", upload_to=""),
        ),
    ]
