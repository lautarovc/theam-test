# Generated by Django 3.0.8 on 2020-07-21 19:35

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='photo',
            field=models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to=''),
        ),
    ]