# Generated by Django 4.1.5 on 2023-01-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='image',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='video',
            field=models.TextField(default='[]'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='videoPhoto',
            field=models.TextField(default='[]'),
        ),
    ]
