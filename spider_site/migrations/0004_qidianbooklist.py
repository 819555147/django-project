# Generated by Django 2.0.3 on 2018-04-11 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_site', '0003_auto_20180330_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='QiDianBookList',
            fields=[
                ('Title', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Author', models.CharField(max_length=15)),
                ('Link', models.URLField()),
                ('Description', models.TextField()),
            ],
        ),
    ]
