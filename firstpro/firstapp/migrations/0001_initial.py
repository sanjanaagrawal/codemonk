# Generated by Django 3.0.2 on 2020-01-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='modeltable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=264)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=264)),
            ],
        ),
    ]
