# Generated by Django 3.1.2 on 2020-11-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201106_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(upload_to='blog images'),
        ),
    ]