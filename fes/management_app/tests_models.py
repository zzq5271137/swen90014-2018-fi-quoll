from django.test import TestCase

from .models import *

import datetime

"""
Created by Zhengqin Zhu.

Models automatic testing:
This file is meant to do some automatically unit testing on models.
It can be run by typing the command "python manage.py test management_app.tests_models" in console.
"""


class ModelTest(TestCase):
    def setUp(self):
        Course.objects.create(id=1, course_name='test course',
                              jsa_required=True, attendee_required=True,
                              customer_sign_required=False)
        Qualification.objects.create(id=1,
                                     qualification_name='test qualification')
        Trainer.objects.create(id=1, trainer_first_name='firstname',
                               trainer_last_name='lastname',
                               trainer_register_number='abc',
                               trainer_email='test@gmail.com',
                               trainer_home_phone='123',
                               trainer_work_phone='456')
        time = datetime.datetime(2018, 5, 27, 12, 20,
                                 tzinfo=datetime.timezone.utc)
        Client.objects.create(id=1, client_name='unimelb', contact_name='mark',
                              contact_email='mark@gmail.com',
                              created_time=time)
        client = Client.objects.get(id=1)
        ClientAddress.objects.create(client=client, street='street',
                                     state='state',
                                     postcode=123)
        trainer = Trainer.objects.get(id=1)
        InventoryItem.objects.create(item_code='abc123', item_type=1,
                                     item_status=1,
                                     item_taken=time)
        item = InventoryItem.objects.get(item_code='abc123')
        InventoryInteraction.objects.create(id=1, item=item, trainer=trainer,
                                            taken_date=time,
                                            status_at_that_time=1)

    def test_course_model(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.course_name, 'test course')
        self.assertTrue(course.jsa_required)
        self.assertTrue(course.attendee_required)
        self.assertFalse(course.customer_sign_required)

    def test_qualification_model(self):
        qualification = Qualification.objects.get(id=1)
        self.assertEqual(qualification.qualification_name, 'test qualification')

    def test_trainer_model(self):
        trainer = Trainer.objects.get(id=1)
        self.assertEqual(trainer.trainer_first_name, 'firstname')
        self.assertEqual(trainer.trainer_last_name, 'lastname')
        self.assertEqual(trainer.trainer_register_number, 'abc')
        self.assertEqual(trainer.trainer_email, 'test@gmail.com')
        self.assertEqual(trainer.trainer_home_phone, '123')
        self.assertEqual(trainer.trainer_work_phone, '456')

    def test_client_model(self):
        time = datetime.datetime(2018, 5, 27, 12, 20,
                                 tzinfo=datetime.timezone.utc)
        client = Client.objects.get(id=1)
        self.assertEqual(client.client_name, 'unimelb')
        self.assertEqual(client.contact_name, 'mark')
        self.assertEqual(client.contact_email, 'mark@gmail.com')
        self.assertEqual(client.created_time, time)

    def test_clientaddress_model(self):
        clientaddress = ClientAddress.objects.get(client=1)
        self.assertEqual(clientaddress.street, 'street')
        self.assertEqual(clientaddress.state, 'state')
        self.assertEqual(clientaddress.postcode, 123)

    def test_inventoryitem_model(self):
        time = datetime.datetime(2018, 5, 27, 12, 20,
                                 tzinfo=datetime.timezone.utc)
        # trainer = Trainer.objects.get(id=1)
        inventory_item = InventoryItem.objects.get(item_code='abc123')
        self.assertEqual(inventory_item.item_type, 1)
        self.assertEqual(inventory_item.item_status, 1)
        # self.assertEqual(inventoryItem.item_trainer, trainer)
        self.assertEqual(inventory_item.item_taken, time)

    def test_inventory_interaction(self):
        time = datetime.datetime(2018, 5, 27, 12, 20,
                                 tzinfo=datetime.timezone.utc)
        inventory_interaction = InventoryInteraction.objects.get(id=1)
        item = InventoryItem.objects.get(item_code='abc123')
        trainer = Trainer.objects.get(id=1)
        self.assertEqual(inventory_interaction.item, item)
        self.assertEqual(inventory_interaction.trainer, trainer)
        self.assertEqual(inventory_interaction.taken_date, time)
        self.assertEqual(inventory_interaction.status_at_that_time, 1)
