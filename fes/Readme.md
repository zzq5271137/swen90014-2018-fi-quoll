# The FES web app

The application is designed for the admin users at FES. Admin user can use this to do Create/Read/Update/Delete operations on Trainer, Class, Courses, Clients, etc.

## Getting Started

This application make use of Django 2.0.8, for other external library dependencies, please check fes/requirement.txt

If you are unfamiliar with Django, there are two main "apps"(modules) in this application, admin_entrance and management_app.
Please check 
```
management_app/views.py 
management_app/urls.py
management_app/models.py
management_app/forms.py
management_app/templates folder
```
Automatic testings can be found in 
```
tests_forms.py
tests_views.py
tests_models.py
```
### Prerequisites
Set up MySQL locally, for more instructions, please check deployment_instructions.pdf

To install other dependencies, set up your virtual environment first, then run

```
pip install requirements
```
this command would check all the libraries listed in requirements.txt and install automatically.

### Run it on your computer
To test the application on your own computer first, go to the directory with manage.py file, then

```
python manage.py migrate
python manage.py runserver
```
the migrate command would create required database(please make sure your have create a user called "fesadmin" in MySQL already)
The application should be accessible on localhost:8000 using the runserver command.

You do not have a user account yet, ctrl+c in your terminal to stop the application,
```
python manage.py createsuperuser
```
to create your first account, and using python manage.py runserver to run it again.
You should now be able to log in with the account you just created.

## Running the tests

To run unit tests, you have to make sure your have your database configured according to my.cnf
the user "fesadmin" should have permissions to create test database.

### Test all

You can run all the tests using

```
python manage.py test
```

### Test specific file

You can run specific test file using, e.g.

```
python manage.py test tests_forms.py
```

## Deployment
Brief steps are as follow, for more specific instructions, please check deployment_instructions.pdf
1. Provision your own AWS server
2. Install LEMP stack on server
3. Set up nginx + uWSGI
4. Create the database and user
5. Set up python virtual environment
6. Run the application as Daemon

## Authors
Wenqiang Kuang

Zhengqing Zhu