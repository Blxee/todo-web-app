# Generated by Django 4.0.5 on 2022-10-25 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_todo_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
