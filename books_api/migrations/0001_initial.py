# Generated by Django 4.0.1 on 2022-01-18 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
            ],
        ),
    ]
