# Generated by Django 4.2.1 on 2023-05-12 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_subject_remove_task_created_remove_task_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='tasks.subject'),
        ),
    ]