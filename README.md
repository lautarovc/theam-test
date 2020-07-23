# theam-test

## Getting Started
The requirements.txt file contains all the Python3 packages needed to run the project.

The following Environment Variables need to be defined:
<ul>
  <li>DB_PASSWORD: The database user password.</li>
  <li>SECRET_KEY: Django's secret key.</li>
  <li>GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE_CONTENTS: The contents of the Google Drive Json Key File. Visit https://django-googledrive-storage.readthedocs.io/ for more information.</li>
</ul>

<p>The project is already configured to run on a PostgreSQL database called "theam-test" with the user "theam-test" running on localhost. This can be changed in the settings.py file inside the theamTest folder.</p>

## Local Installation
* Inside the project's folder run:
    >pip3 install -r requirements.txt
* Create the database "theam-test" with owner "theam-test" on your local PostgreSQL manager.
* Inside the project's folder run:
    >python3 manage.py migrate
* Create a superuser by following the steps after running:
    >python3 manage.py createsuperuser
* Run the server on the default address and port (127.0.0.1:8000):
    >python3 manage.py runserver

## API Endpoints
### Getting the Client Id and Client Secret key
You can register and manage an application to obtain the client id and client secret key by entering to the _/rest/oauth/applications/_ module through the browser.

### OAuth
You can obtain an access token by making a POST call to the _/rest/oauth/token/_ endpoint with the client id and client secret key, and the following data:

* grant_type=password
* username=[any username]
* password=[user's password]

For example, with CURL:

>curl -X POST -d "grant_type=password&username=[username]&password=[password]" -u "[Client ID]:[Client Secret]" http://[host]:[port]/rest/oauth/token/

**--INSERT TABLE WITH ALL POSSIBLE OUTPUTS--**

### User Management
Only a user that has the _is_staff_ attribute as true can List, Get, Create, Edit, Update and Delete users. The superuser by default can do this.

All the following endpoints can only be accessed by having the current user's Access Token in the header, in CURL:
>-H "Authorization: Bearer [ACCESS TOKEN]"

#### List Users
To list all users, you can make a GET call to the _/rest/users/_ endpoint, in CURL:

>curl -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/

**--INSERT TABLE WITH ALL POSSIBLE OUTPUTS--**

#### Create User
To create a user, you can make a POST call to the _/rest/users/_ endpoint with the following data:

* username=[any username]
* first_name=[user's name]
* last_name=[user's surname]
* email=[user's email]
* is_staff=[true|false if admin]
* password=[user's password]

For example, with CURL:

>curl -X POST -d '{"username":"user1", "first_name":"", "last_name":"", "email":"", "is_staff":false, "password":"123456"}' -H "Content-Type: application/json" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/

**--INSERT TABLE WITH ALL POSSIBLE OUTPUTS--**

#### Get User
To get a specific user, you can make a GET call to the _/rest/users/[USER ID]/_ endpoint, in CURL:

>curl -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/[USER ID]/

**--INSERT TABLE WITH ALL POSSIBLE OUTPUTS--**

#### Edit User
To edit all of a user's data, you can make a PUT call to the _/rest/users/[USER ID]/_ endpoint with the following data:

* username=[any username]
* first_name=[user's name]
* last_name=[user's surname]
* email=[user's email]
* is_staff=[true|false if admin]
* password=[user's password]

For example, with CURL:

>curl -X PUT -d '{"username":"user1", "first_name":"", "last_name":"", "email":"", "is_staff":false}' -H "Content-Type: application/json" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/[USER ID]/

**--INSERT TABLE WITH ALL POSSIBLE OUTPUTS--**

#### Update User Attribute
To update one or more attributes from a user, you can make a PATCH call to the _/rest/users/[USER ID]/_ endpoint with any of the following variables as data:

* username=[any username]
* first_name=[user's name]
* last_name=[user's surname]
* email=[user's email]
* is_staff=[true|false if admin]
* password=[user's password]

For example, with CURL:

>curl -X PATCH -d '{"first_name":"name1","is_staff":false}' -H "Content-Type: application/json" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/[USER ID]/

**--INSERT TABLE WITH ALL POSSIBLE OUTPUTS--**

#### Delete User
To delete a user, you can make a DELETE call to the _/rest/users/[USER ID]/_ endpoint, in CURL:

>curl -X DELETE -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/[USER ID]/

**--INSERT TABLE WITH ALL POSSIBLE OUTPUTS--**

