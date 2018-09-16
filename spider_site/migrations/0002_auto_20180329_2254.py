# Generated by Django 2.0.3 on 2018-03-29 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider_site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SegmentFault',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.CharField(max_length=30)),
                ('Link', models.CharField(max_length=300)),
                ('Answers', models.IntegerField()),
                ('Content', models.TextField()),
                ('ScrapyDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='segmentfault',
            unique_together={('Item', 'ScrapyDate')},
        ),
    ]
