# Generated by Django 4.1.7 on 2023-06-29 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='img',
            field=models.ImageField(default=1, upload_to='imgs/food/'),
            preserve_default=False,
        ),
    ]