# Generated by Django 3.1.2 on 2020-10-31 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to=None)),
                ('date', models.DateField()),
            ],
        ),
    ]
