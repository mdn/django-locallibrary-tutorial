# Generated by Django 2.1.5 on 2020-11-16 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0097_auto_20201116_0719'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_category_table_entry',
            old_name='t_category_table_id',
            new_name='t_category_table',
        ),
        migrations.RenameField(
            model_name='t_conflict',
            old_name='priorization_conflict_workpackage_id_one',
            new_name='priorization_conflict_workpackage_one',
        ),
        migrations.RenameField(
            model_name='t_conflict',
            old_name='priorization_conflict_workpackage_id_two',
            new_name='priorization_conflict_workpackage_two',
        ),
    ]
