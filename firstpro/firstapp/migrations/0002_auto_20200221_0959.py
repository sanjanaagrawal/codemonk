# Generated by Django 3.0.2 on 2020-02-21 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modeltable',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='modeltable',
            name='Password',
        ),
        migrations.RemoveField(
            model_name='modeltable',
            name='Username',
        ),
        migrations.AddField(
            model_name='modeltable',
            name='description',
            field=models.CharField(default='pqr', max_length=264),
        ),
        migrations.AddField(
            model_name='modeltable',
            name='directions',
            field=models.CharField(default='pqr', max_length=264),
        ),
        migrations.AddField(
            model_name='modeltable',
            name='image',
            field=models.FileField(default='firstpro/static/pallav_resume.pdf', upload_to='fileupload'),
        ),
        migrations.AddField(
            model_name='modeltable',
            name='ingredients',
            field=models.CharField(default='pqr', max_length=264),
        ),
        migrations.AddField(
            model_name='modeltable',
            name='name',
            field=models.CharField(default='pqr', max_length=264),
        ),
        migrations.AddField(
            model_name='modeltable',
            name='time',
            field=models.CharField(default='pqr', max_length=264),
        ),
    ]
