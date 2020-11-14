# Generated by Django 2.1.5 on 2020-11-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0048_auto_20201114_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='created_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='is_workpackage',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='memorization_sequence',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='memorization_sequence_is_fixed_because_memorized',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='relevantinformation_comment',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='bookinstance',
            name='updated_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]