from datetimewidget.widgets import DateTimeWidget
from django import forms
from django.forms import formset_factory
from schedule.models import Calendar

from .models import Client, Course, Qualification, Trainer, FesClass, \
    ClientAddress, InventoryItem, Attendee

""" 
Created by Wenqiang Kuang
The management_app forms

This lists all the forms used by templates. User uses forms to submit inputs to make GET/POST requests to the server. 
Each class represents a form, fields are the neeeded inputs.
"""


class NewTrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = (
            'trainer_first_name', 'trainer_last_name',
            'trainer_register_number',
            'trainer_email',
            'trainer_work_phone', 'trainer_qualification',)
        widgets = {
            'trainer_qualification': forms.CheckboxSelectMultiple(
                attrs={'class': 'trainer_qualifications'})
        }
        

class NewClientAddressForm(forms.ModelForm):
    class Meta:
        model = ClientAddress
        fields = field = ('street', 'state', 'postcode')


class NewClassForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NewClassForm, self).__init__(*args, **kwargs)
        self.fields['calendar'].queryset = Calendar.objects.filter(slug="classCalendar")

    class Meta:
        model = FesClass
        fields = (
            'start', 'end', 'class_course', 'title',
            'class_trainer', 'class_client', 'calendar',
            'class_location',)
        widgets = {
            'start': DateTimeWidget(attrs={'id': "start_end"}, usel10n=True,
                                    bootstrap_version=3),
            'end': DateTimeWidget(attrs={'id': "start_end"}, usel10n=True,
                                  bootstrap_version=3),
        }


class NewAttendeeForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ('first_name', 'last_name',)


AttendeeFormSet = formset_factory(NewAttendeeForm)


class NewCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_name', 'jsa_required', 'attendee_required',
                  'customer_sign_required')


class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('client_name', 'contact_name', 'contact_email',)


class NewQualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ('qualification_name', 'course_teachable',)
        widgets = {
            'course_teachable': forms.CheckboxSelectMultiple(
                attrs={'class': 'myfieldclass'})
        }


class EditInventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ('item_status', 'item_taken', 'taken_trainer')
        widgets = {
            'item_taken': DateTimeWidget(attrs={'id': "start_end"},
                                         usel10n=True,
                                         bootstrap_version=3),
            'taken_trainer': forms.CheckboxSelectMultiple()
        }


class NewInventoryItemForm(forms.ModelForm):
    class Meta:
        model = InventoryItem
        fields = ('item_code', 'item_status', 'item_type')
