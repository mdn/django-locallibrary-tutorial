# Generated by Django 2.1.5 on 2020-11-12 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_author_week_target_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='memorizable_workpackage_relevantinformation_tobememorized',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='target_group_question',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
