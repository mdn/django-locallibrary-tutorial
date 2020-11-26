# Generated by Django 2.1.5 on 2020-11-25 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0138_auto_20201125_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_Wt_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday_Timeseries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(blank=True, null=True)),
                ('week_target_isnot_potential_day_target_on_weekday_date', models.DateField(blank=True, null=True)),
                ('t_week_target', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Author')),
            ],
            options={
                'db_table': 't_wt_is_excluded_from_dt_mp_assignment_on_weekday_timeseries',
                'ordering': ['created_datetime'],
            },
        ),
    ]