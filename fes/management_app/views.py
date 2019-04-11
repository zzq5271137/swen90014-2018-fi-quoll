from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.utils import timezone
from schedule.models import Event, Calendar

from management_app.search import ClassFilter
from .forms import NewClientForm, NewCourseForm, NewQualificationForm, \
    NewTrainerForm, NewClassForm, \
    NewClientAddressForm, EditInventoryItemForm, NewInventoryItemForm, \
    AttendeeFormSet
from .models import Client, Course, Qualification, Trainer, FesClass, \
    InventoryItem, Attendee, InventoryInteraction

""" 
Created by Wenqiang Kuang on Oct 1st 2018 
The management_app views

This defines all the functions used to request data from database. 
Context represents data derived from MySQL, it is then rendered within a html page. 

Every function is named explicitly by its functionality. 
e.g. "classes" represent the all the classes
     "class_detail" shows all attributes in a class object
     "class_add" add a class in the database
     "class_delete" delete a class from the database
     "class_edit" would firstly load the specified class, then allow user to modify it attributes with form. 
"""


def homepage(request):
    all_events = Event.objects.all()
    template = loader.get_template('management_app/homepage.html')

    context = {
        'all_events': all_events,
    }
    return HttpResponse(template.render(context, request))


# --------------------------Class------------------------------------
def classes(request):
    all_classes = Event.objects.all
    template = loader.get_template('management_app/classes.html')

    context = {
        'class_list': all_classes,
    }
    return HttpResponse(template.render(context, request))


def class_detail(request, class_id):
    fes_class = get_object_or_404(FesClass, pk=class_id)
    template = loader.get_template('management_app/class_detail.html')

    context = {
        'class': fes_class,
    }
    return HttpResponse(template.render(context, request))


def class_add(request):
    the_big_calendar = get_object_or_404(Calendar, slug="classCalendar")
    if request.method == "POST":
        class_form = NewClassForm(request.POST)
        attendee_formset = AttendeeFormSet(request.POST)

        if class_form.is_valid() and attendee_formset.is_valid():
            class_form.fields["calendar_id"] = the_big_calendar.id
            fes_class = class_form.save(commit=False)
            fes_class.save()
            attendee_list = []
            for attendee_form in attendee_formset:
                attendee = attendee_form.save(commit=False)
                attendee.class_attend = fes_class
                attendee.save()
                attendee_list.append(attendee)

            return redirect(class_detail, fes_class.id)
    else:
        class_form = NewClassForm()
        attendee_formset = AttendeeFormSet()

    context = {
        'class_form': class_form,
        'attendee_formset': attendee_formset
    }

    return render(request, 'management_app/class_add_new_class.html', context)


def class_edit(request, class_id):
    fes_class = get_object_or_404(FesClass, pk=class_id)
    all_attendee = Attendee.objects.filter(class_attend=fes_class).values()

    if request.method == "POST":
        class_form = NewClassForm(request.POST, instance=fes_class)
        attendee_formset = AttendeeFormSet(request.POST, initial=all_attendee)

        if class_form.is_valid() and attendee_formset.is_valid():
            fes_class = class_form.save(commit=False)
            fes_class.save()

            Attendee.objects.filter(class_attend=fes_class).delete()
            for attendee_form in attendee_formset:
                attendee = attendee_form.save(commit=False)
                attendee.class_attend = fes_class
                attendee.save()
            return redirect(class_detail, fes_class.id)
    else:
        class_form = NewClassForm(instance=fes_class)
        attendee_formset = AttendeeFormSet(initial=all_attendee)

    context = {
        'class_form': class_form,
        'attendee_formset': attendee_formset,
    }

    return render(request, 'management_app/class_add_new_class.html', context)


def class_delete(request, class_id):
    fes_class = get_object_or_404(FesClass, pk=class_id)
    fes_class.delete()
    return redirect(classes)


# --------------------------Trainer------------------------------------
def trainers(request):
    all_trainers = Trainer.objects.all
    template = loader.get_template('management_app/trainers.html')

    context = {
        'trainer_list': all_trainers,
    }
    return HttpResponse(template.render(context, request))


def trainer_detail(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    template = loader.get_template('management_app/trainer_detail.html')

    context = {
        'trainer': trainer,
    }
    return HttpResponse(template.render(context, request))


def trainer_timetable(request, trainer_id):
    #trainer = get_object_or_404(Trainer, pk=trainer_id)
    calendar = Calendar.objects.filter(slug="classCalendar")
    template = loader.get_template('management_app/trainer_timetable.html')

    context = {
        'calendar': calendar,
    }
    return HttpResponse(template.render(context, request))


def trainer_add(request):
    if request.method == "POST":
        trainer_form = NewTrainerForm(request.POST)
        #trainer_calendar_form = NewCalendarForm(request.POST)
        #if all((trainer_form.is_valid(), trainer_calendar_form.is_valid())):
        if (trainer_form.is_valid()):
            trainer = trainer_form.save(commit=False)
            trainer.save()
            #calendar = trainer_calendar_form.save(commit=False)
            #calendar.trainer = trainer
            #calendar.save()
            trainer_form.save_m2m()
            return redirect(trainer_detail, trainer.id)
    else:
        trainer_form = NewTrainerForm()
        #trainer_calendar_form = NewCalendarForm()

    context = {
        'trainer_form': trainer_form,
        #'trainer_calendar_form': trainer_calendar_form
    }
    return render(request, 'management_app/trainer_add_new_trainer.html',
                  context)


def trainer_edit(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    trainer_calendar = trainer.calendar
    if request.method == "POST":
        trainer_form = NewTrainerForm(request.POST, instance=trainer)
        #trainer_calendar_form = NewCalendarForm(request.POST, instance=trainer_calendar)
        #if all((trainer_form.is_valid(), trainer_calendar_form.is_valid())):
        if (trainer_form.is_valid()):
            trainer = trainer_form.save(commit=False)
            trainer.save()
            #calendar = trainer_calendar_form.save(commit=False)
            #calendar.trainer = trainer
            #calendar.save()
            trainer_form.save_m2m()
            return redirect(trainer_detail, trainer.id)
    else:
        trainer_form = NewTrainerForm(instance=trainer)
        #trainer_calendar_form = NewCalendarForm(instance=trainer_calendar)

    context = {
        'trainer_form': trainer_form,
        #'trainer_calendar_form': trainer_calendar_form
    }
    return render(request, 'management_app/trainer_add_new_trainer.html',
                  context)


def trainer_delete(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    trainer.delete()
    return redirect(trainers)


# --------------------------Course------------------------------------
def courses(request):
    all_courses = Course.objects.all
    template = loader.get_template('management_app/courses.html')

    context = {
        'course_list': all_courses,
    }
    return HttpResponse(template.render(context, request))


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    template = loader.get_template('management_app/course_detail.html')

    context = {
        'course': course,
    }
    return HttpResponse(template.render(context, request))


def course_add(request):
    if request.method == "POST":
        form = NewCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect(course_detail, course.id)
    else:
        form = NewCourseForm()
    return render(request, 'management_app/course_add_new_course.html',
                  {'form': form})


def course_edit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == "POST":
        form = NewCourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            return redirect('course_detail', course.id)
    else:
        form = NewCourseForm(instance=course)
    return render(request, 'management_app/course_add_new_course.html',
                  {'form': form})


def course_delete(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    return redirect(courses)


# --------------------------Client------------------------------------
def clients(request):
    all_clients = Client.objects.all
    template = loader.get_template('management_app/clients.html')

    context = {
        'client_list': all_clients,
    }
    return HttpResponse(template.render(context, request))


def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    template = loader.get_template('management_app/client_detail.html')

    context = {
        'client': client,
    }
    return HttpResponse(template.render(context, request))


def client_add(request):
    if request.method == "POST":
        client_form = NewClientForm(request.POST)
        address_form = NewClientAddressForm(request.POST)
        if all((client_form.is_valid(), address_form.is_valid())):
            client = client_form.save(commit=False)
            client.created_time = timezone.now()
            client.save()
            address = address_form.save(commit=False)
            address.client = client
            address_form.save()
            return redirect(client_detail, client.id)
    else:
        client_form = NewClientForm()
        address_form = NewClientAddressForm()
    return render(request, 'management_app/client_add_new_client.html',
                  {'client_form': client_form, 'address_form': address_form})


def client_edit(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    address = client.address
    if request.method == "POST":
        client_form = NewClientForm(request.POST, instance=client)
        address_form = NewClientAddressForm(request.POST, instance=address)
        if all((client_form.is_valid(), address_form.is_valid())):
            client = client_form.save(commit=False)
            client.created_time = timezone.now()
            client.save()
            address = address_form.save(commit=False)
            address.client = client
            address_form.save()
            return redirect('client_detail', client.id)
    else:
        client_form = NewClientForm(instance=client)
        address_form = NewClientAddressForm(instance=address)
    return render(request, 'management_app/client_add_new_client.html',
                  {'client_form': client_form, 'address_form': address_form})


def client_delete(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    client.delete()
    return redirect(clients)


# --------------------------Qualification------------------------------------
def qualifications(request):
    all_qualifications = Qualification.objects.all
    template = loader.get_template('management_app/qualifications.html')

    context = {
        'qualification_list': all_qualifications,
    }
    return HttpResponse(template.render(context, request))


def qualification_detail(request, qualification_id):
    qualification = get_object_or_404(Qualification, pk=qualification_id)
    template = loader.get_template('management_app/qualification_detail.html')

    context = {
        'qualification': qualification,
    }
    return HttpResponse(template.render(context, request))


def qualification_add(request):
    if request.method == "POST":
        form = NewQualificationForm(request.POST)
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.save()
            form.save_m2m()
            return redirect(qualification_detail, qualification.id)
    else:
        form = NewQualificationForm()
    return render(request,
                  'management_app/qualification_add_new_qualification.html',
                  {'form': form})


def qualification_edit(request, qualification_id):
    qualification = get_object_or_404(Qualification, pk=qualification_id)
    if request.method == "POST":
        form = NewQualificationForm(request.POST, instance=qualification)
        if form.is_valid():
            qualification = form.save(commit=False)
            qualification.save()
            form.save_m2m()
            return redirect('qualification_detail', qualification.id)
    else:
        form = NewQualificationForm(instance=qualification)
    return render(request,
                  'management_app/qualification_add_new_qualification.html',
                  {'form': form})


def qualification_delete(request, qualification_id):
    qualification = get_object_or_404(Qualification, pk=qualification_id)
    qualification.delete()
    return redirect(qualifications)


# --------------------------Inventory------------------------------------
def inventoryitems(request):
    all_inventoryitems = InventoryItem.objects.all
    template = loader.get_template('management_app/inventoryitems.html')

    context = {
        'inventoryitem_list': all_inventoryitems,
    }
    return HttpResponse(template.render(context, request))


def inventoryitem_detail(request, item_code):
    inventoryitem = get_object_or_404(InventoryItem, pk=item_code)
    template = loader.get_template('management_app/inventoryitem_detail.html')

    context = {
        'inventoryitem': inventoryitem,
    }
    return HttpResponse(template.render(context, request))


def inventoryitem_add(request):
    if request.method == "POST":
        form = NewInventoryItemForm(request.POST)
        if form.is_valid():
            inventoryitem = form.save(commit=False)
            inventoryitem.save()
            return redirect(inventoryitem_detail, inventoryitem.item_code)
    else:
        form = NewInventoryItemForm()
    return render(request,
                  'management_app/inventoryitem_add_new_inventoryitem.html',
                  {'item_form': form})


def inventoryitem_edit(request, item_code):
    inventoryitem = get_object_or_404(InventoryItem, pk=item_code)
    if request.method == "POST":
        edit_item_form = EditInventoryItemForm(request.POST, instance=inventoryitem)
        if edit_item_form.is_valid():
            inventoryitem = edit_item_form.save(commit=False)
            inventoryitem.save()
            taken_date = request.POST.get('item_taken')
            trainer_id = request.POST.get('taken_trainer')
            status = request.POST.get('item_status')
            taken_by = Trainer.objects.get(id=trainer_id)
            new_history = InventoryInteraction(item=inventoryitem,
                                               trainer=taken_by,
                                               taken_date=taken_date,
                                               status_at_that_time=status)
            new_history.save()
            return redirect('inventoryitem_detail', item_code)
    else:
        edit_item_form = EditInventoryItemForm(instance=inventoryitem)
    return render(request,
                  'management_app/inventoryitem_add_new_inventoryitem.html',
                  {'item_form': edit_item_form})


def inventoryitem_delete(request, item_code):
    inventoryitem = get_object_or_404(InventoryItem, pk=item_code)
    inventoryitem.delete()
    return redirect(inventoryitems)


def inventory_interaction(request, item_code):
    item_history = InventoryInteraction.objects.filter(item_id=item_code)
    template = loader.get_template(
        'management_app/inventoryitem_interaction_history.html')

    context = {
        'item_history_list': item_history,
    }
    return HttpResponse(template.render(context, request))


# --------------------------Timesheets------------------------------------

def timesheet_search(request):
    all_classes = FesClass.objects.all()
    class_filter = ClassFilter(request.GET, queryset=all_classes)
    class_filter_form = class_filter.form

    context = {
        'class_filter_form': class_filter_form,
        'class_filter': class_filter,
    }
    return render(request, 'management_app/timesheets_search.html', context)
