# Generated by Django 2.1.4 on 2019-01-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Diabetes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diabetes',
            name='Outcome',
            field=models.DecimalField(decimal_places=4, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]