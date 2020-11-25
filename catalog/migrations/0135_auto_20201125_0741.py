# Generated by Django 2.1.5 on 2020-11-25 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0134_auto_20201123_2236'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='t_day_target_sequence_timeseries',
            options={'ordering': ['sequence_proposed_for_day_target_memory_palace']},
        ),
        migrations.AddField(
            model_name='t_day_target_sequence_timeseries',
            name='t_memorization_package_memory_palace_or_cards_technique',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Memorization_Package_Memory_Palace_Or_Cards_Technique'),
        ),
        migrations.AddField(
            model_name='t_day_target_sequence_timeseries',
            name='t_memory_palace_type_location_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Memory_Palace_Type_Location_Number'),
        ),
        migrations.AddField(
            model_name='t_day_target_sequence_timeseries',
            name='t_week_target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Author'),
        ),
    ]
