# Generated by Django 2.1.5 on 2020-11-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_remove_book_is_shown_at_next_time_measurement_stop'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='associated_email_subject',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
