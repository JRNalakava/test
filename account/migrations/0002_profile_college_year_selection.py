# Generated by Django 2.2.2 on 2019-06-13 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='college_year_selection',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'Freshman'), (1, 'Sophomore'), (2, 'Junior'), (3, 'Senior')], null=True),
        ),
    ]
