# Generated by Django 3.2.4 on 2022-03-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0044_remove_store_qob_soni'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=2, default=0, max_digits=155)),
                ('naqd_pull_sum', models.DecimalField(decimal_places=2, default=0, max_digits=155)),
                ('naqd_pull_dollor', models.DecimalField(decimal_places=2, default=0, max_digits=155)),
            ],
            options={
                'verbose_name_plural': 'Ikkkinchi Kassa',
            },
        ),
    ]
