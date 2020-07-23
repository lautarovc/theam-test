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
