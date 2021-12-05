# Generated by Django 3.2.9 on 2021-12-05 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.ForeignKey(default='beginner', on_delete=django.db.models.deletion.CASCADE, to='accounts.typeprofile', to_field='name'),
        ),
        migrations.AlterField(
            model_name='typeprofile',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]