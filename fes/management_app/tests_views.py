from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

"""
Created by Wenqiang Kuang

Views automatic testing:
This tests nine important views (the login, client_list, tainer_list, class_list pages etc. ) after successfully 
loging into the system. 

Run it by typing the command "python manage.py test management_app.tests_views" in terminal.
"""


class ViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

    def test_login(self):
        response = self.client.post('/', follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_login_uses_correct_template(self):
        response = self.client.get(reverse('homepage'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'management_app/homepage.html')

    def test_login_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_client_list_page(self):
        response = self.client.get(reverse('client_list'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'management_app/clients.html')

    def test_trainer_list_page(self):
        response = self.client.get(reverse('trainer_list'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'management_app/trainers.html')

    def test_qualification_list_page(self):
        response = self.client.get(reverse('qualification_list'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'management_app/qualifications.html')

    def test_class_list_page(self):
        response = self.client.get(reverse('class_list'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'management_app/classes.html')

    def test_course_list_page(self):
        response = self.client.get(reverse('course_list'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'management_app/courses.html')

    def test_inventoryitem_list_page(self):
        response = self.client.get(reverse('inventoryitem_list'), follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'management_app/inventoryitems.html')

