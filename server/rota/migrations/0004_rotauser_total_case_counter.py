# Generated by Django 5.0.2 on 2024-03-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rota', '0003_cases_temporary_assignee_alter_rotauser_is_next_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='rotauser',
            name='total_case_counter',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]