from django import forms
from django.forms import ModelForm
from .models import Msg
from django import forms

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

class CustomerForm(ModelForm):
    msg_study = forms.ChoiceField(choices=STUDY_CHOICES, widget=forms.RadioSelect)
    msg_blood = forms.BooleanField(label="Blut")
    msg_stool = forms.BooleanField(label="Stuhl")
    msg_urin = forms.BooleanField(label="Urin")
    msg_room = forms.ChoiceField(choices=ROOM_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Msg
        fields = ['msg_study', 'msg_blood',  'msg_stool',  'msg_urin', 'msg_room']
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CustomerForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['msg_blood'].required = False
        self.fields['msg_stool'].required = False
        self.fields['msg_urin'].required = False