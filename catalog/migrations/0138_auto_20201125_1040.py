# Generated by Django 2.1.5 on 2020-11-25 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0137_auto_20201125_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_week_target_is_excluded_from_dt_mp_assignment_on_weekday',
            name='t_week_target',
        ),
        migrations.DeleteModel(
            name='T_Week_Target_Is_Excluded_From_Dt_Mp_Assignment_On_Weekday',
        ),
    ]
