# Generated by Django 4.1.7 on 2023-10-08 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_comment_comment_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]