# Generated by Django 3.2.7 on 2022-04-22 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20220422_0639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='why_did_learn_or_are_interested_in_ar',
        ),
        migrations.AddField(
            model_name='applicant',
            name='why_learn_or_are_inwhy_learn_or_are_interested_in_arterested_in_ar',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]
