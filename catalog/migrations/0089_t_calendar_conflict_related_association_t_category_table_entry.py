# Generated by Django 2.1.5 on 2020-11-15 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0088_t_conflict_priorization_conflict_workpackage_id_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='t_calendar_conflict_related_association',
            name='t_category_table_entry',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.t_category_table_entry'),
        ),
    ]
