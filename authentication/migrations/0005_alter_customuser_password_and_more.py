# Generated by Django 4.1.2 on 2022-10-20 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_customuser_mobile_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='scout_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
