# Generated by Django 3.2.4 on 2022-05-26 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0104_remove_order_date_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
