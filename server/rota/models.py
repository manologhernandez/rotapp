from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class RotaUser(models.Model):
    STATUS_CHOICES = (
        ('AVL', 'Follow the Sun'),
        ('OOO', 'Out of Office'),
        ('BRK', 'Break/Lunch'),
        ('QMR', 'On Queue Management'),
        ('WRP', 'Wrap Up'),
        ('BSY', 'Busy'),
        ('TRN', 'Training')
    )
    REGION_CHOICES = (
        ('EMEA', 'Europe, Middle East, and Africa'),
        ('APAC', 'Asia - Pacific'),
        ('AMERS', 'Americas')
    )
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    user_status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='OOO')
    user_region = models.CharField(max_length=120, choices=REGION_CHOICES, default='APAC')
    new_case_counter = models.IntegerField(default=0, null=True, blank=True)
    fts_case_counter = models.IntegerField(default=0, null=True, blank=True)
    closed_case_counter = models.IntegerField(default=0, null=True, blank=True)
    cancelled_case_counter = models.IntegerField(default=0, null=True, blank=True)
    transferred_case_counter = models.IntegerField(default=0, null=True, blank=True)   
    daily_case_counter = models.IntegerField(default=0, null=True, blank=True)
    is_next_case = models.BooleanField(default=True)
    total_case_counter = models.IntegerField(default=0, null=True, blank=True)

class Cases(models.Model):
    STATUS_CHOICES = (
		('FTS', 'Follow the Sun'),
		('NewCase', 'New Case'),
        ('Closed', 'Closed Case'),
        ('Cancelled', 'Cancelled'),
        ('Transferred', 'Transferred')
	)
    assignee = models.ForeignKey(RotaUser, related_name="of_user", on_delete=models.CASCADE)
    case_number = models.IntegerField(default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    case_status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='NewCase')
    temporary_assignee = models.CharField(max_length=25, default='')
