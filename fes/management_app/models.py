from django.db import models
from schedule.models import Event, Calendar

""" 
Created by Wenqiang Kuang
The management_app models

This defines all the models used to do ORM(object relational mapping), which is used to interact with application data 
from MySQL. 

Every class represents a model, which is a table in the database. 
Many-to-Many relationships are resolved automatically by Django using an associative table. 
"""


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=100)
    created_time = models.DateTimeField('date added')

    def __str__(self):
        return self.client_name


class ClientAddress(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE,
                                  primary_key=True, related_name='address')
    street = models.CharField(max_length=50)
    state = models.CharField(max_length=5)
    postcode = models.IntegerField()


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    jsa_required = models.BooleanField()
    attendee_required = models.BooleanField()
    customer_sign_required = models.BooleanField()

    def __str__(self):
        return self.course_name


class Qualification(models.Model):
    qualification_name = models.CharField(max_length=100)
    course_teachable = models.ManyToManyField(Course)

    def __str__(self):
        return self.qualification_name


class Trainer(models.Model):
    trainer_first_name = models.CharField(max_length=50)
    trainer_last_name = models.CharField(max_length=50)
    trainer_register_number = models.CharField(max_length=100)
    trainer_email = models.CharField(max_length=100)
    trainer_work_phone = models.CharField(max_length=20)
    trainer_home_phone = models.CharField(max_length=20)
    trainer_qualification = models.ManyToManyField(Qualification)

    def __str__(self):
        return "%s %s" % (self.trainer_first_name, self.trainer_last_name)


class FesClass(Event):
    class_location = models.CharField(max_length=100)
    class_trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='fesclass')
    class_client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='fesclass')
    class_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='fesclass')
    note = models.CharField(max_length=200, null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    feedback = models.CharField(max_length=200, null=True, blank=True)
    jsa_committed = models.BooleanField(default=False)
    signed = models.BooleanField(default=False)


class Attendee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    class_attend = models.ForeignKey(FesClass, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class TrainerCalendar(Calendar):
    trainer = models.OneToOneField(Trainer, on_delete=models.CASCADE,
                                   primary_key=True, related_name='calendar')


class InventoryItem(models.Model):
    item_code = models.CharField(max_length=50, primary_key=True)
    types = (
        (1, 'Water Extinguisher'),
        (2, 'CO2 Extinguisher'),
        (3, 'Foam Extinguisher')
    )
    status = (
        (1, 'new'),
        (2, 'used'),
        (3, 'exhausted')
    )
    item_type = models.IntegerField(choices=types)
    item_status = models.IntegerField(choices=status)
    item_taken = models.DateTimeField('date taken', null=True)
    taken_trainer = models.ManyToManyField(Trainer,
                                           through='InventoryInteraction')


class InventoryInteraction(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    taken_date = models.DateTimeField()
    status = (
        (1, 'new'),
        (2, 'used'),
        (3, 'exhausted')
    )
    status_at_that_time = models.IntegerField(choices=status)
