# Generated by Django 2.0.3 on 2018-04-26 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_site', '0004_qidianbooklist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segmentfault',
            old_name='Answers',
            new_name='Author',
        ),
        migrations.AddField(
            model_name='segmentfault',
            name='Tag',
            field=models.CharField(default=2, max_length=30),
            preserve_default=False,
        ),
    ]
