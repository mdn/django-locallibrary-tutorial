# Generated by Django 2.1.5 on 2020-11-16 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0098_auto_20201116_0720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt',
            old_name='t_calendar_conflict_related_association_id',
            new_name='t_calendar_conflict_related_association',
        ),
        migrations.RenameField(
            model_name='t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt',
            old_name='t_conflict_id',
            new_name='t_conflict',
        ),
        migrations.RenameField(
            model_name='t_calendar_conflict_related_association',
            old_name='t_calendar_id',
            new_name='t_calendar_foreignkey',
        ),
        migrations.RenameField(
            model_name='t_calendar_conflict_related_association',
            old_name='t_conflict_id',
            new_name='t_conflict',
        ),
        migrations.RenameField(
            model_name='t_calendar_conflict_related_association',
            old_name='t_memorization_package_memory_palace_technique_id',
            new_name='t_memorization_package_memory_palace_technique',
        ),
    ]