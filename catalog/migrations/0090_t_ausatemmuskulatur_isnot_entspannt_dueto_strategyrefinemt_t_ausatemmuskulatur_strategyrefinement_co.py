# Generated by Django 2.1.5 on 2020-11-15 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0089_t_calendar_conflict_related_association_t_category_table_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt',
            name='t_ausatemmuskulatur_strategyrefinement_conflict_phase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Ausatemmuskulatur_Strategyrefinement_Conflict_Phase'),
        ),
    ]