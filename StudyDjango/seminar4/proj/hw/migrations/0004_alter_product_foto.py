# Generated by Django 4.2.6 on 2023-10-31 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw', '0003_product_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='foto',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
