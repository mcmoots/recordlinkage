# Generated by Django 2.0.1 on 2018-01-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matcher', '0003_auto_20180125_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordmatch',
            name='score',
            field=models.DecimalField(decimal_places=3, default=2.8, max_digits=10),
            preserve_default=False,
        ),
    ]
