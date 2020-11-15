# Generated by Django 2.1.5 on 2020-11-15 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0080_auto_20201115_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_memory_palace_memorization_timeseries',
            name='t_calendar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Calendar'),
        ),
        migrations.AddField(
            model_name='t_memory_palace_memorization_timeseries',
            name='t_memory_palace_memorization_timeseries_action',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Memory_Palace_Memorization_Timeseries_Action'),
        ),
    ]