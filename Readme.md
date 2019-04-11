This project is consist of two parts, the web application and the mobile application. 

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


# FES Mobile Application

[![Version](https://img.shields.io/npm/v/react-native-calendars.svg)](https://www.npmjs.com/package/react-native-calendars)
[![Build Status](https://travis-ci.org/wix/react-native-calendars.svg?branch=master)](https://travis-ci.org/wix/react-native-calendars)

The package is both **Android** and **iOS** compatible.

#### Deployment Instruction - Mobile App

This page is created for `Mobile App` deployment.
This remote server for this is shared with web app side.
The cloud server we choose is AWS's free trial server, whose type is t2.micro.
The operation system for the server is Ubuntu 16.04.

You need to be a developer for iOS in order to publish this app to the marketplace. Therefore, we provide the client with an alternative method to run it.
To run and deploy this mobile app, please follow the instructions below.

##### Installing Dependencies
The framework of this app is `React-Native` proposed by Facebook. Therefore, basic prerequisites plugins should be installed.

###### Node, Watchman
We recommend installing `Node` and `Watchman` using `Homebrew`.
Run the following commands in a Terminal after installing Homebrew:
```
brew install node
brew install watchman
```
If you have already installed `Node` on your system, make sure it is `Node 8.3` or newer.

###### The React Native CLI
Node comes with `npm`, which lets you install the React Native command line interface.
Run the following command in a Terminal:
```
npm install -g react-native-cli
```
###### Xcode
The easiest way to install Xcode is via the Mac App Store. Installing Xcode will also install the iOS Simulator and all the necessary tools to build your iOS app.

#### Fetch the Code
In order to run the app on your `iPhone` or a `simulator`, please git the code from `Bitbucket` or download from `Google Drive`.
##### Method 1: Bitbucket
#
```
git clone https://yunpengw1@bitbucket.cis.unimelb.edu.au:8445/scm/swen900142018fiquoll/swen90014-2018-fi-quoll.git
```
Pros:
Shorter time to download.

Cons:
Components might conflict.
More time needed to install component.
Manually configuration needed.
##### Method 2: Google Drive
#
```
https://drive.google.com/file/d/12_unOtDAvIE_zKC28lkT3C0K4m42Tjlf/view?usp=sharing
```
Pros:
Best way to run Mobile App without error.
Environment configured in the zip.
Components chosen are compatible.
Cons
File is large.

`Run the Code`
1. Open the workspace with Xcode.
The route should be something like this:
~react-native-calendars/example/ios/CalendarsExample.xcodeproj

2. Add an Account before building the App.
We need to add an apple account to Xcode to run the App because of safety reasons.
Simply click on 'Add an Account...' from 'General' tag above and type in the account you have.


3. Choose a real/virtual device test.
On the top left, you can decide whether to use a real device or iOS simulator to run the App.


4. Run the App
Simply press 'Command+R' to run the App.

`Troubleshooting`
There might be several reasons which can lead to the failure of mobile app running.
Most solutions can be found through Stack-overflow.
For my experience, it happens when you build it with different version of operating system and Xcode.
In Xcode 10, the following step helps to solve 90% of the problem which might happen in the procedure.


## Authors
* Yunpeng Wang
* Haonan Chen
* [Tautvilas Mecinskas](https://github.com/tautvilas/) - Initial code - [@tautvilas](https://twitter.com/TautviIas)
* Katrin Zotchev - Initial design - [@katrin_zot](https://twitter.com/katrin_zot)

## Contributing

Pull requests are welcome. `npm run test` and `npm run lint` before push.

