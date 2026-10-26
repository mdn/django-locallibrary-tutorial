# Django Local Library

Tutorial "Local Library" website written in Django.

For detailed information about this project see the associated [MDN tutorial home page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website).

## Overview

This web application creates an online catalog for a small local library, where users can browse available books and manage their accounts.

The main features that have currently been implemented are:

- There are models for books, book copies, genre, language and authors.
- Users can view list and detail information for books and authors.
- Admin users can create and manage models. The admin has been optimised (the basic registration is present in admin.py, but commented out).
- Librarians can renew reserved books.

![Local Library Model](https://raw.githubusercontent.com/mdn/django-locallibrary-tutorial/master/catalog/static/images/local_library_model_uml.png)

## Quick Start

To get this project up and running locally on your computer:

1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/development_environment).
   > **Note:** This has been tested against Django 6.1, which requires Python 3.12 or later.
2. Create and activate a Python virtual environment for the project using [venv](https://docs.python.org/3/library/venv.html), the virtual environment tool built into Python:

   ```
   # Linux/macOS
   python3 -m venv django6_env
   source django6_env/bin/activate

   # Windows
   py -3 -m venv django6_env
   django6_env\Scripts\activate
   ```

3. Assuming your virtual environment is active, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python` to start Python):

   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```

4. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
5. Create a few test objects of each type.
6. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
