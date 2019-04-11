from django.urls import path

from . import views

""" 
Created by Wenqiang Kuang on Oct 1st 2018 
The management_app urls

This lists all the url paths used in the web app. 
The jinja template language would get the corresponding view via either "name" or path
e.g. href="{% url 'course_list' %}" makes use of the "name"
     href="/management_app/trainers" makes use of the full path
"""

urlpatterns = [
    path('', views.homepage, name='homepage'),

    # trainer list page
    path('trainers', views.trainers, name='trainer_list'),

    # trainer detail page
    path('trainers/<int:trainer_id>/', views.trainer_detail,
         name='trainer_detail'),

    # trainer timetable page
    path('trainers/<int:trainer_id>/timetable', views.trainer_timetable,
         name='trainer_timetable'),

    # add new trainer page
    path('trainers/new', views.trainer_add, name='trainer_add'),

    # edit a trainer page
    path('trainers/<int:trainer_id>/edit', views.trainer_edit,
         name='trainer_edit'),

    # delete a trainer page
    path('trainers/<int:trainer_id>/delete', views.trainer_delete,
         name='trainer_delete'),

    # course list page
    path('courses', views.courses, name='course_list'),

    # course detail page
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),

    # add new course page
    path('courses/new', views.course_add, name='course_add'),

    # edit a course page
    path('courses/<int:course_id>/edit', views.course_edit, name='course_edit'),

    # delete a course page
    path('courses/<int:course_id>/delete', views.course_delete,
         name='course_delete'),

    # class list page
    path('classes', views.classes, name='class_list'),

    # class detail page
    path('classes/<int:class_id>/', views.class_detail, name='class_detail'),

    # add new class page
    path('classes/new', views.class_add, name='class_add'),

    # edit a class page
    path('classes/<int:class_id>/edit', views.class_edit, name='class_edit'),

    # delete a class page
    path('classes/<int:class_id>/delete', views.class_delete,
         name='class_delete'),

    # client list page
    path('clients', views.clients, name='client_list'),

    # client detail page
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),

    # add new client page
    path('clients/new', views.client_add, name='client_add'),

    # edit a client page
    path('clients/<int:client_id>/edit', views.client_edit, name='client_edit'),

    # delete a client page
    path('clients/<int:client_id>/delete', views.client_delete,
         name='client_delete'),

    # qualification list page
    path('qualifications', views.qualifications, name='qualification_list'),

    # qualification detail page
    path('qualifications/<int:qualification_id>/', views.qualification_detail,
         name='qualification_detail'),

    # add new qualification page
    path('qualifications/new', views.qualification_add,
         name='qualification_add'),

    # edit a qualification page
    path('qualifications/<int:qualification_id>/edit', views.qualification_edit,
         name='qualification_edit'),

    # delete a qualification page
    path('qualifications/<int:qualification_id>/delete',
         views.qualification_delete, name='qualification_delete'),

    # inventory items list page
    path('inventoryitems', views.inventoryitems, name='inventoryitem_list'),

    # inventory item detail page
    path('inventoryitems/<item_code>/', views.inventoryitem_detail,
         name='inventoryitem_detail'),

    # add new inventory item page
    path('inventoryitems/new', views.inventoryitem_add,
         name='inventoryitem_add'),

    # edit a inventory item page
    path('inventoryitems/<item_code>/edit', views.inventoryitem_edit,
         name='inventoryitem_edit'),

    # delete an item page
    path('inventoryitems/<item_code>/delete',
         views.inventoryitem_delete, name='inventoryitem_delete'),

    # timesheet search result page
    path('timesheet_search', views.timesheet_search, name='timesheet_search'),

    # interaction between one item and trainers page
    path('iteminteraction/<item_code>/', views.inventory_interaction,
         name='item_interaction'),
]
