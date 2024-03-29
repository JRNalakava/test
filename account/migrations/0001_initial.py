# Generated by Django 2.2.2 on 2019-06-14 22:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('img_src', models.URLField(blank=True, null=True)),
                ('philanthropy_req', models.IntegerField(default='0')),
                ('professional_req', models.IntegerField(default='0')),
                ('tech_req', models.IntegerField(default='0')),
                ('financial_req', models.BooleanField(default=False)),
                ('pledge_class', models.TextField(max_length=5)),
                ('college_year_selection', models.PositiveSmallIntegerField(choices=[(0, 'Freshman'), (1, 'Sophomore'), (2, 'Junior'), (3, 'Senior')], default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
