# Generated by Django 4.0.4 on 2022-06-20 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('user_idx', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=100, unique=True)),
                ('user_pw', models.CharField(max_length=100)),
            ],
        ),
    ]
