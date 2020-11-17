# Generated by Django 2.1.5 on 2020-11-15 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0090_t_ausatemmuskulatur_isnot_entspannt_dueto_strategyrefinemt_t_ausatemmuskulatur_strategyrefinement_co'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_memorization_package_memory_palace_technique',
            name='t_conflict_strategy_category_measure_foreignkey',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Conflict_Strategy_Category_Measure'),
        ),
        migrations.AddField(
            model_name='t_memorization_package_memory_palace_technique',
            name='t_memory_palace_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Memory_Palace_Type'),
        ),
    ]