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
    new_case_counter = models.IntegerField(default=0, null=True, blank=True) # MY TOTAL CASE WILL BE NEW CASE + CLOSED CASE
    fts_case_counter = models.IntegerField(default=0, null=True, blank=True) # FTS CASES WILL BE COUNTED IN NEW CASES/OPEN CASE BUT WILL RESET ON THE NEXT DAY
    close_case_counter = models.IntegerField(default=0, null=True, blank=True)
    cancelled_case_counter = models.IntegerField(default=0, null=True, blank=True) # MY CANCELLED AND TRANSFERRED CASE WILL BE SUBTRACTED TO MY NEW CASE 
    transferred_case_counter = models.IntegerField(default=0, null=True, blank=True)



class Cases(models.Model):
    STATUS_CHOICES = (
		('fts', 'Follow the Sun'),
		('newcase', 'New Case/Open Case'),
        ('closed', 'Closed Case'),
        ('cancelled', 'Cancelled'),
        ('transferred', 'Transferred')
	)
    assignee = models.ForeignKey(RotaUser, related_name="of_user", on_delete=models.CASCADE)
    case_number = models.IntegerField(default=0, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    case_status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='NewCase')



