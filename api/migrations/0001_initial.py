# Generated by Django 4.1.5 on 2023-01-09 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addtime', models.DateTimeField()),
                ('maximage', models.CharField(max_length=255, unique=True)),
                ('minimage', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': '相约',
                'verbose_name_plural': '相约',
                'db_table': 'appointment',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addtime', models.DateTimeField()),
                ('maximage', models.CharField(max_length=255, unique=True)),
                ('minimage', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': '孩童',
                'verbose_name_plural': '孩童',
                'db_table': 'child',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addtime', models.DateTimeField()),
                ('maximage', models.CharField(max_length=255, unique=True)),
                ('minimage', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': '家庭',
                'verbose_name_plural': '家庭',
                'db_table': 'family',
            },
        ),
        migrations.CreateModel(
            name='GourmetFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addtime', models.DateTimeField()),
                ('maximage', models.CharField(max_length=255, unique=True)),
                ('minimage', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': '美食',
                'verbose_name_plural': '美食',
                'db_table': 'gourmetFood',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openId', models.CharField(max_length=255, unique=True)),
                ('nickName', models.CharField(default='用户', max_length=255)),
                ('addTime', models.DateTimeField()),
                ('userImage', models.CharField(default='static/set/user.png', max_length=255)),
                ('heartWallpaper', models.TextField(default='[]')),
                ('writeBackgroundWallpaper', models.CharField(blank=True, max_length=255)),
                ('readBackgroundWallpaper', models.CharField(blank=True, max_length=255)),
                ('diaryCount', models.IntegerField(default=0)),
                ('diaryPassword', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary', models.TextField()),
                ('video', models.TextField(blank=True)),
                ('videoPhoto', models.TextField(blank=True)),
                ('image', models.TextField(blank=True)),
                ('writeTime', models.DateTimeField()),
                ('mood', models.CharField(max_length=20)),
                ('weather', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.user')),
            ],
            options={
                'verbose_name': '用户日记',
                'verbose_name_plural': '用户日记',
                'db_table': 'diary',
                'managed': True,
            },
        ),
    ]
