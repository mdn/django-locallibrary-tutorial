# Generated by Django 2.1.5 on 2020-11-13 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0029_book_hyperlink_for_readiness_enhancement'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_shown_at_next_time_measurement_stop',
            field=models.IntegerField(null=True, default=None, max_length=19),
        ),
    ]
