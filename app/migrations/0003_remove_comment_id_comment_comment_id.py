# Generated by Django 4.1.7 on 2023-10-08 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_comment_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_id',
            field=models.IntegerField(default=True, primary_key=True, serialize=False),
        ),
    ]
