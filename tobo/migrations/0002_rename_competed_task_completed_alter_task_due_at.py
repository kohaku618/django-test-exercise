# Generated by Django 5.0.6 on 2024-06-27 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tobo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='competed',
            new_name='completed',
        ),
        migrations.AlterField(
            model_name='task',
            name='due_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
