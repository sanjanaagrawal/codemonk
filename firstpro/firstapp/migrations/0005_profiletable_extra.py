# Generated by Django 3.0.2 on 2020-02-21 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20200221_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiletable',
            name='extra',
            field=models.CharField(default='mno', max_length=264),
        ),
    ]
