# Generated by Django 2.1.5 on 2020-11-13 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_auto_20201113_0747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='week_target_comment',
            new_name='filepath_for_readiness_enhancement',
        ),
    ]
