# Generated by Django 2.1.5 on 2020-11-20 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0118_auto_20201120_1039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='t_memory_palace_type',
            options={'ordering': ['memory_palace_type']},
        ),
    ]
