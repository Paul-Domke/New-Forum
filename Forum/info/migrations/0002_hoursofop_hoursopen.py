# Generated by Django 2.2.6 on 2020-05-19 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoursOpen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], unique=True)),
                ('hour_start', models.TimeField()),
                ('hours_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HoursOfOp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50)),
                ('hours', models.ManyToManyField(related_name='hours', to='info.HoursOpen')),
            ],
        ),
    ]
