# Generated by Django 5.0.6 on 2024-06-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0004_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='slider/')),
            ],
        ),
    ]
