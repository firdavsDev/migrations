# Generated by Django 3.2.4 on 2022-05-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0107_alter_aktwagon_bunker'),
    ]

    operations = [
        migrations.AddField(
            model_name='bunker',
            name='fakt_neto',
            field=models.IntegerField(default=0),
        ),
    ]
