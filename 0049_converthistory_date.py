# Generated by Django 3.2.4 on 2022-03-03 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_auto_20220303_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='converthistory',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
