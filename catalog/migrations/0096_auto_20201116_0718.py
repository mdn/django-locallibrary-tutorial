# Generated by Django 2.1.5 on 2020-11-16 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0095_auto_20201116_0714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='t_information_item_tobeoperationalized_memor_timeseries',
            old_name='t_information_item_tobeoperationalized_id',
            new_name='t_information_item_tobeoperationalized',
        ),
    ]