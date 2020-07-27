# theam-test

# Getting Started
The requirements.txt file contains all the Python3 packages needed to run the project.

The following Environment Variables need to be defined:
<ul>
  <li>DB_PASSWORD: The database user password.</li>
  <li>SECRET_KEY: Django's secret key.</li>
  <li>GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE_CONTENTS: The contents of the Google Drive Json Key File. Visit https://django-googledrive-storage.readthedocs.io/ for more information.</li>
  <li>TEST_INFO: <b>Only for the tests module.</b> Json object with the following structure:</li>
</ul>

```
{
    "cId": Client Id Key,
    "cS": Client Secret Key,
    "adminUser": Admin username,
    "adminPass": Admin password,
    "normalUser": Normal User username,
    "normalPass": Normal User password,
    "URL": URL of your deployed app
}
```

<p>The project is already configured to run on a PostgreSQL database called "theam-test" with the user "theam-test" running on localhost. This can be changed in the settings.py file inside the theamTest folder.</p>

# Local Installation
* Inside the project's folder run:
    >pip3 install -r requirements.txt
* Create the database "theam-test" with owner "theam-test" on your local PostgreSQL manager.
* Inside the project's folder run:
    >python3 manage.py migrate
* Create a superuser by following the steps after running:
    >python3 manage.py createsuperuser
* Run the server on the default address and port (127.0.0.1:8000):
    >python3 manage.py runserver

# API Endpoints
## Getting the Client Id and Client Secret key
### Endpoint: /rest/oauth/applications/
You can register and manage an application to obtain the client id and client secret key by entering to the _/rest/oauth/applications/_ module through the **browser**.


## OAuth
### Endpoint: /rest/oauth/token/
You can obtain an access token by making a **POST** request to the _/rest/oauth/token/_ endpoint with the client id and client secret key, and the following data:

* grant_type=password
* username=[any username]
* password=[user's password]

For example, with CURL:

>curl -X POST -d "grant_type=password&username=[username]&password=[password]" -u "[Client ID]:[Client Secret]" http://[host]:[port]/rest/oauth/token/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     200       | JSON object with keys: <br>{"access_token","expires_in", "token_type", "scope", "refresh_token"} | Successful call, returns new token
|     400       | JSON object: <br>{"error": "invalid_grant", "error_description": "Invalid credentials given."} | Invalid credentials, wrong username or pasword.
|     401       | JSON object: <br> {"error": "invalid_client"} | Invalid Client Id or Client Secret key

## Headers
**Content-Type:** All the endpoints below are compatible with the _application/json_ and _multipart/form-data_ media types. For uploading photos, always use _multipart/form-data_. For GET requests, you can omit this header.

**Authorization:** All the following endpoints can only be accessed by having this header, which must include the Access Token of the current user, written in the following syntax: _Bearer [ACCESS TOKEN]_


## User Management
Only a user that has the _is_staff_ attribute as true can List, Get, Create, Edit, Update and Delete users. The superuser by default can do this.

**The User object:**
```
{
    "id": <auto int>,
    "username": <str>,
    "first_name": <str>,
    "last_name": <str>,
    "email": <str>,
    "is_staff": <bool>
}
```
### Endpoint: /rest/users/
#### List Users (GET)
To list all users, you can make a **GET** request to the _/rest/users/_ endpoint, in CURL:

>curl -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     200       | JSON object with keys:<br>{"count","next","previous","results": Array of User objects} | Successful call, returns array of User objects
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     403       | JSON object: <br>{"detail":"You do not have permission to perform this action."} | Current user has no permission to access this resource.


#### Create User (POST)
To create a user, you can make a **POST** request to the _/rest/users/_ endpoint with the following data:

* username=[any username]
* first_name=[user's name]
* last_name=[user's surname]
* email=[user's email]
* is_staff=[true|false if admin]
* password=[user's password]

For example, with CURL:

>curl -X POST -d '{"username":"user1", "first_name":"", "last_name":"", "email":"", "is_staff":false, "password":"123456"}' -H "Content-Type: application/json" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     201       | New User object | Successful call, returns the newly created User object.
|     400       | JSON object with the required fields errors | Unsuccessful call, field errors (e.g: Unique username, username not provided).
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     403       | JSON object: <br>{"detail":"You do not have permission to perform this action."} | Current user has no permission to access this resource.


### Endpoint: /rest/users/[USER ID]/
#### Get User (GET)
To get a specific user, you can make a **GET** request to the _/rest/users/[USER ID]/_ endpoint, in CURL:

>curl -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/[USER ID]/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     200       | User object | Successful call, returns the User object.
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     403       | JSON object: <br>{"detail":"You do not have permission to perform this action."} | Current user has no permission to access this resource.
|     404       | JSON object: <br>{"detail":"Not found."} | User ID not found


#### Edit User (PUT)
To edit all of a user's data, you can make a **PUT** request to the _/rest/users/[USER ID]/_ endpoint with the following data:

* username=[any username]
* first_name=[user's name]
* last_name=[user's surname]
* email=[user's email]
* is_staff=[true|false if admin]
* password=[user's password]

For example, with CURL:

>curl -X PUT -d '{"username":"user1", "first_name":"", "last_name":"", "email":"", "is_staff":false}' -H "Content-Type: application/json" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/[USER ID]/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     201       | Edited User object | Successful call, returns the edited User object.
|     400       | JSON object with the required fields errors | Unsuccessful call, field errors (e.g: Unique username, username not provided).
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     403       | JSON object: <br>{"detail":"You do not have permission to perform this action."} | Current user has no permission to access this resource.
|     404       | JSON object: <br>{"detail":"Not found."} | User ID not found


#### Update User Attribute (PATCH)
To update one or more attributes from a user, you can make a **PATCH** request to the _/rest/users/[USER ID]/_ endpoint with any of the following variables as data:

* username=[any username]
* first_name=[user's name]
* last_name=[user's surname]
* email=[user's email]
* is_staff=[true|false if admin]
* password=[user's password]

For example, with CURL:

>curl -X PATCH -d '{"first_name":"name1","is_staff":false}' -H "Content-Type: application/json" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/[USER ID]/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     201       | Edited User object | Successful call, returns the edited User object.
|     400       | JSON object with the required fields errors | Unsuccessful call, field errors (e.g: Unique username).
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     403       | JSON object: <br>{"detail":"You do not have permission to perform this action."} | Current user has no permission to access this resource.
|     404       | JSON object: <br>{"detail":"Not found."} | User ID not found


#### Delete User (DELETE)
To delete a user, you can make a **DELETE** request to the _/rest/users/[USER ID]/_ endpoint, in CURL:

>curl -X DELETE -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/users/[USER ID]/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     204       | None | Successful call, User deleted.
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     403       | JSON object: <br>{"detail":"You do not have permission to perform this action."} | Current user has no permission to access this resource.
|     404       | JSON object: <br>{"detail":"Not found."} | User ID not found


### Customer Management
All users can List, Get, Create, Edit, Update and Delete customers.

**The Customer object:**
```
{
    "id": <str>,
    "name": <str>,
    "surname": <str>,
    "photo": <URL>,
    "createdBy": <int>,
    "lastUpdatedBy": <int>
}
```

### Endpoint: /rest/customers/
#### List Customers (GET)
To list all customers, you can make a **GET** request to the _/rest/customers/_ endpoint, in CURL:

>curl -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/customers/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     200       | JSON object with keys:<br>{"count","next","previous","results": Array of Customer objects} | Successful call, returns array of Customer objects
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.


#### Create Customers (POST)
To create a customer, you can make a **POST** request to the _/rest/customers/_ endpoint with the following data:

**Required**
* id=[customer's id]
* name=[customer's name]
* surname=[customer's surname]
**Optional**
* photo=@[URL/Path to photo]

For example, with CURL:

>curl -X POST -d '{"id":"1234", "name":"name1", "surname":"name1"}' -H "Content-Type: application/json" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/customers/

Or, with the photo attribute:

>curl -X POST -F id=1234 -F name=name1 -F surname=name1 -F photo=@/path/to/photo.jpg -H "Content-Type: multipart/form-data" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/customers/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     201       | New Customer object | Successful call, returns the newly created Customer object.
|     400       | JSON object with the required fields errors | Unsuccessful call, field errors (e.g: Required field not provided, unique Id error).
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.


### Endpoint: /rest/customers/[CUSTOMER ID]/
#### Get Customer (GET)
To get a specific customer, you can make a **GET** request to the _/rest/customers/[CUSTOMER ID]/_ endpoint, in CURL:

>curl -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/customers/[CUSTOMER ID]/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     200       | User object | Successful call, returns the Customer object.
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     404       | JSON object: <br>{"detail":"Not found."} | Customer ID not found

#### Edit Customer (PUT)
To edit all of a customer's data, you can make a **PUT** request to the _/rest/customers/[CUSTOMER ID]/_ endpoint with the following data:

**Required**
* id=[customer's id]
* name=[customer's name]
* surname=[customer's surname]
**Optional (note that if it's not included, it will be replaced by null**
* photo=@[URL/Path to photo]

For example, with CURL:

>curl -X PUT -d '{"id":"1234", "name":"name1", "surname":"name1"}' -H "Content-Type: application/json" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/customers/[CUSTOMER ID]/

Or, with the photo attribute:

>curl -X PUT -F id=1234 -F name=name1 -F surname=name1 -F photo=@/path/to/photo.jpg -H "Content-Type: multipart/form-data" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/customers/[CUSTOMER ID]/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     201       | Edited Customer object | Successful call, returns the edited Customer object.
|     400       | JSON object with the required fields errors | Unsuccessful call, field errors (e.g: Required field not provided, unique Id error).
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     404       | JSON object: <br>{"detail":"Not found."} | Customer ID not found


#### Update Customer Attribute (PATCH)
To update one or more attributes from a customer, you can make a **PATCH** request to the _/rest/customers/[CUSTOMER_ID]/_ endpoint with any of the following variables as data:

* id=[customer's id]
* name=[customer's name]
* surname=[customer's surname]
* photo=@[URL/Path to photo]

For example, with CURL:

>curl -X PATCH -d '{"name":"name1","surname":"name1"}' -H "Content-Type: application/json" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/customers/[CUSTOMER ID]/

Or, with the photo attribute:

>curl -X PATCH -F photo=@path/to/photo.jpg -H "Content-Type: multipart/form-data" -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/customers/[CUSTOMER ID]/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     201       | Edited Customer object | Successful call, returns the edited Customer object.
|     400       | JSON object with the required fields errors | Unsuccessful call, field errors (e.g: Unique Id).
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     404       | JSON object: <br>{"detail":"Not found."} | Customer ID not found


#### Delete Customer (DELETE)
To delete a customer, you can make a **DELETE** request to the _/rest/customers/[CUSTOMER ID]/_ endpoint, in CURL:

>curl -X DELETE -H "Authorization: Bearer [ACCESS TOKEN]" http://[host]:[port]/rest/customers/[CUSTOMER ID]/

**Possible Outputs**

| Status Code   | Response Content| Description   |
| ------------- | -------------   | ------------- |
|     204       | None | Successful call, Customer deleted.
|     401       | JSON object: <br>{"detail":"Authentication credentials were not provided."} | Invalid or no token provided.
|     404       | JSON object: <br>{"detail":"Not found."} | Customer ID not found

