# Generated by Django 2.2 on 2020-01-14 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ogames', '0002_auto_20200114_0115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athleteevent',
            name='city',
        ),
        migrations.RemoveField(
            model_name='athleteevent',
            name='game',
        ),
        migrations.RemoveField(
            model_name='athleteevent',
            name='season',
        ),
        migrations.RemoveField(
            model_name='athleteevent',
            name='sport',
        ),
        migrations.RemoveField(
            model_name='athleteevent',
            name='year',
        ),
        migrations.AddField(
            model_name='athlete',
            name='sport',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ogames.Sport'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ogames.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ogames.Game'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='season',
            field=models.CharField(default='Summer', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
