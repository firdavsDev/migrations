# Generated by Django 3.2.4 on 2022-04-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0095_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(blank=True, default=1, help_text='50kg = 1qob', null=True),
        ),
    ]
