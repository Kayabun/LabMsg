from django.db import models

#TYPE_CHOICES = (
#	('blut','Blut'),
#    ('stuhl', 'Stuhl'),
#    ('urin','Urin'),
#)

STUDY_CHOICES = (
	('NAKO','NAKO'),
    ('RESIST', 'RESIST'),
)

ROOM_CHOICES = (
	('Labor','Labor'),
    ('U1','U1'),
    ('U2','U2'),
    ('U3','U3'),
    ('U4','U4'),
)

# Create your models here.
class Msg(models.Model):
    msg_study = models.CharField(max_length=200, choices=STUDY_CHOICES, null=True, blank=True)
    msg_blood = models.BooleanField(default=False)
    msg_stool = models.BooleanField(default=False)
    msg_urin = models.BooleanField(default=False)
    msg_room = models.CharField(max_length=200, choices=ROOM_CHOICES, null=True, blank=True)
    msg_date = models.DateTimeField(auto_now_add=True, blank=True)
    msg_mark = models.BooleanField(default=False)
    msg_count = models.IntegerField(blank=True, null=True)


    #def __str__(self):
    #    return self.msg_count 

