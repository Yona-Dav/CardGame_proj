# Generated by Django 3.2.9 on 2021-12-06 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_picture.jpg', upload_to='profile_pic/'),
        ),
    ]
