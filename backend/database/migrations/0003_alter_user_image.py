# Generated by Django 4.1.3 on 2022-11-20 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
