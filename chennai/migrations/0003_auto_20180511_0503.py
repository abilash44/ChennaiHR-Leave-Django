# Generated by Django 2.0.5 on 2018-05-10 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chennai', '0002_auto_20180511_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveformmodel',
            name='hr_approved_time_stamp',
            field=models.DateTimeField(null=True),
        ),
    ]