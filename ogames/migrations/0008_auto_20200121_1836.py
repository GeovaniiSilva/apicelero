# Generated by Django 2.2.9 on 2020-01-21 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogames', '0007_auto_20200121_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]