# Generated by Django 2.1.5 on 2020-11-22 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0131_auto_20201122_2134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='t_category_table_predicate_asverb',
            options={'ordering': ['predicate_asverb']},
        ),
    ]
