# Generated by Django 3.2.4 on 2022-03-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_merge_20220301_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='entered_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='left_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='turned_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
