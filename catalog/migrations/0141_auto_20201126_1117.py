# Generated by Django 2.1.5 on 2020-11-26 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0140_remove_t_calendar_t_category_table_entry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_wt_or_wp_or_infotbo_category_timeseries',
            name='t_category_table',
        ),
        migrations.RemoveField(
            model_name='t_wt_or_wp_or_infotbo_category_timeseries',
            name='t_category_table_entry',
        ),
        migrations.RemoveField(
            model_name='t_wt_or_wp_or_infotbo_category_timeseries',
            name='t_information_item_tobeoperationalized',
        ),
        migrations.RemoveField(
            model_name='t_wt_or_wp_or_infotbo_category_timeseries',
            name='t_week_target',
        ),
        migrations.RemoveField(
            model_name='t_wt_or_wp_or_infotbo_category_timeseries',
            name='t_workpackage',
        ),
        migrations.DeleteModel(
            name='T_Wt_Or_Wp_Or_Infotbo_Category_Timeseries',
        ),
    ]