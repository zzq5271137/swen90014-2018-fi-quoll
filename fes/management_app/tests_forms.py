from django.test import TestCase

from .forms import *
from .models import *

import datetime

"""
Created by Zhengqin Zhu.

Forms automatic testing:
This file is meant to do some automatically unit testing on forms.
It can be run by typing the command "python manage.py test management_app.tests_forms" in console.
"""


class NewCourseFormTest(TestCase):

    def test_NewCourseForm_valid(self):
        form = NewCourseForm(
            data={'course_name': "Course 1", 'jsa_required': True,
                  'attendee_required': True, 'customer_sign_required': True})
        self.assertTrue(form.is_valid())

    def test_NewCourseForm_invalid(self):
        form = NewCourseForm(
            data={'course_name': "", 'jsa_required': True,
                  'attendee_required': True, 'customer_sign_required': True})
        self.assertFalse(form.is_valid())


class NewTrainerFormTest(TestCase):

    def setUp(self):
        self.qualification = Qualification.objects.create(id=1,
                                                          qualification_name='test qualification')

    def test_NewTrainerForm_invalid(self):
        form = NewTrainerForm(
            data={'trainer_first_name': "", 'trainer_last_name': "Zhu",
                  'trainer_register_number': "123",
                  'trainer_email': "zzq@gmail.com",
                  'trainer_work_phone': "123",
                  'trainer_qualification': self.qualification.pk})
        self.assertFalse(form.is_valid())


class NewClientAddressFormTest(TestCase):

    def test_NewClientAddressForm_valid(self):
        form = NewClientAddressForm(
            data={'street': "abc", 'state': "def", 'postcode': 123})
        self.assertTrue(form.is_valid())

    def test_NewClientAddressForm_invalid(self):
        form = NewClientAddressForm(
            data={'street': "abc", 'state': "", 'postcode': 123})
        self.assertFalse(form.is_valid())


class NewAttendeeFormTest(TestCase):

    def test_NewAttendeeForm_valid(self):
        form = NewAttendeeForm(
            data={'first_name': "Zhengqing", 'last_name': "Zhu"})
        self.assertTrue(form.is_valid())

    def test_NewAttendeeForm_invalid(self):
        form = NewAttendeeForm(
            data={'first_name': "", 'last_name': "Zhu"})
        self.assertFalse(form.is_valid())


class NewClientFormTest(TestCase):

    def test_NewClientForm_valid(self):
        form = NewClientForm(
            data={'client_name': "UniMelb", 'contact_name': "Mark",
                  'contact_email': "mark@gmail.com"})
        self.assertTrue(form.is_valid())

    def test_NewClientForm_invalid(self):
        form = NewClientForm(
            data={'client_name': "", 'contact_name': "Mark",
                  'contact_email': "mark@gmail.com"})
        self.assertFalse(form.is_valid())


class NewQualificationFormTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(id=1, course_name='test course',
                                            jsa_required=True,
                                            attendee_required=True,
                                            customer_sign_required=False)

    def test_NewQualificationForm_invalid(self):
        form = NewQualificationForm(
            data={'qualification_name': "",
                  'course_teachable': self.course})
        self.assertFalse(form.is_valid())


class NewInventoryItemFormTest(TestCase):

    def test_NewInventoryItemForm_valid(self):
        form = NewInventoryItemForm(
            data={'item_code': "abc123", 'item_status': 1, 'item_type': 2})
        self.assertTrue(form.is_valid())

    def test_NewInventoryItemForm_invalid(self):
        form = NewInventoryItemForm(
            data={'item_code': "", 'item_status': 1, 'item_type': 2})
        self.assertFalse(form.is_valid())


class EditInventoryItemFormTest(TestCase):
    def setUp(self):
        self.trainer = Trainer.objects.create(id=1,
                                              trainer_first_name='firstname',
                                              trainer_last_name='lastname',
                                              trainer_register_number='abc',
                                              trainer_email='test@gmail.com',
                                              trainer_home_phone='123',
                                              trainer_work_phone='456')

    def test_EditInventoryItemForm_invalid(self):
        time = datetime.datetime(2018, 5, 27, 12, 20,
                                 tzinfo=datetime.timezone.utc)
        form = EditInventoryItemForm(
            data={'item_status': 1, 'item_taken': time,
                  'taken_trainer': self.trainer.pk})
        self.assertFalse(form.is_valid())
