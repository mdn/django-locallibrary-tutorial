# Generated by Django 2.1.5 on 2020-11-15 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0064_t_ausatemmuskulatur_strategyrefinement_conflict_phase'),
    ]

    operations = [
        migrations.CreateModel(
            name='T_Conflict_Strategy_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conflict_strategy_category_verb', models.CharField(default='', max_length=255)),
                ('conflict_strategy_category_mywish', models.CharField(default='', max_length=255)),
            ],
            options={
                'db_table': 't_conflict_strategy_category',
            },
        ),
        migrations.CreateModel(
            name='T_Conflict_Strategy_Category_Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_datetime', models.DateTimeField(blank=True, null=True)),
                ('updated_datetime', models.DateTimeField(blank=True, null=True)),
                ('conflict_strategy_category_measure_description', models.CharField(default='', max_length=255)),
                ('memorization_sequence', models.IntegerField(default=None, null=True)),
                ('memorization_sequence_is_fixed_because_memorized', models.IntegerField(default=None, null=True)),
                ('t_conflict_strategy_category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Conflict_Strategy_Category')),
                ('t_memorization_package_memory_palace_technique_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Memorization_Package_Memory_Palace_Technique')),
                ('t_memory_palace_type_location_number_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.T_Memory_Palace_Type_Location_Number')),
            ],
            options={
                'db_table': 't_conflict_strategy_category_measure',
            },
        ),
    ]
