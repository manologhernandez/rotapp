# Generated by Django 4.2.7 on 2024-02-16 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RotaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_status', models.CharField(choices=[('AVL', 'Follow the Sun'), ('OOO', 'Out of Office'), ('BRK', 'Break/Lunch'), ('QMR', 'On Queue Management'), ('WRP', 'Wrap Up'), ('BSY', 'Busy'), ('TRN', 'Training')], default='OOO', max_length=25)),
                ('user_region', models.CharField(choices=[('EMEA', 'Europe, Middle East, and Africa'), ('APAC', 'Asia - Pacific'), ('AMERS', 'Americas')], default='APAC', max_length=120)),
                ('new_case_counter', models.IntegerField(blank=True, default=0, null=True)),
                ('fts_case_counter', models.IntegerField(blank=True, default=0, null=True)),
                ('close_case_counter', models.IntegerField(blank=True, default=0, null=True)),
                ('cancelled_case_counter', models.IntegerField(blank=True, default=0, null=True)),
                ('transferred_case_counter', models.IntegerField(blank=True, default=0, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.IntegerField(blank=True, default=0, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('case_status', models.CharField(choices=[('fts', 'Follow the Sun'), ('newcase', 'New Case/Open Case'), ('closed', 'Closed Case'), ('cancelled', 'Cancelled'), ('transferred', 'Transferred')], default='NewCase', max_length=25)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='of_user', to='rota.rotauser')),
            ],
        ),
    ]