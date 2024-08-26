# Setting up Django

# Checking Python Installation

```bash
- Open the Command Prompt / Terminal
- Enter the command
> py --version
```

# Setting up virtual environment

Windows

```bash
# Install virtualenv
> pip install virtualenv

# Create a virtual environment
> py -m venv myvenv

# Activate virtual environment
> myvenv\Scripts\activate.bat
```

MacOS

```bash
# Install virtualenv
> pip install virtualenv

# Create a virtual environment
> python -m venv myvenv

# Activate virtual environment
> source myvenv/bin/activate
```

# Install django on virtual python environment

```bash
> pip install django
> python -m django --version
```

# Setting up django project

```bash
> django-admin startproject mysite
> python manage.py runserver
# OR
> python manage.py runserver 8080

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 23, 2024 - 08:48:22
Django version 4.2.13, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# Create app in django project

Create app in the project

```bash
> python manage.py startapp polls
```

Connecting app with the project

ก่อนอื่นเราจะต้องไปแก้ไขค่าตั้งค่าใน `mysite/settings.py` เพื่อให้ Django รู้จักกับ app `polls` ที่เราสร้างขึ้นมาก่อน โดยเพิ่ม "polls" ใน INSTALLED_APPS

```bash
python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Add your apps here
    "polls",
]
```

# Writing View

เปิด web browser และ เข้าไปที่ url `http://localhost:8000/polls/`

Function `path()` นั้นรับ argument 4 ตัว โดยเป็น required argument 2 ตัวได้แก่ `route` และ `view` และเป็น optional argument 2 ตัว ได้แก่ `kwargs` และ `name`

- Argument: `route` - รับค่า string URL patterns
- Argument: `view` - รับ view ที่จะถูกเรียกเมื่อ Django ทำการ match URL pattern ได้
- Argument: `kwargs` - Arbitrary keyword arguments ซึ่งเราสามารถส่ง argument เพิ่มเติมไปยัง view
- Argument: `name` - เป็น string ชื่อของ path URL โดยการตั้งชื่อจะทำให้เราอ้างอิงถึงได้ง่าย เช่นถ้าต้องการ redirect ไปที่ path นี้ก็สามารถอ้างอิงถึงด้วย name แทนที่จะต้องเขียน full path

Creating view file.

```python
# polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

# Routing URL

## Setup routing in **app**

```python
# polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

## Setup routing in project

```python
# mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
```

# Setup database

โดยถ้ายังไม่ได้ทำการติดตั้ง PostgreSQL ให้่สามารถทการติดตั้งก่อน - [POSTGRES DOWNLOAD](https://www.postgresql.org/download/)

จากนั้นทำการติดตั้ง Postgres Client `psycopg2`

## Database Connection

### Accessing postgresql cli

```python
> postgres --version
postgres (PostgreSQL) 15.0
```

### Installing Postgres Client `psycopg2`

```python
> pip install psycopg2
# OR
> pip install psycopg2-binary
# OR
> brew install postgresql # for MacOS
```

### Configure database config

```python
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mypolls",
        "USER": "db_username",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

## Database Server

### Connect to the database using CLI

```bash
> psql -U postgres

/ # psql -U postgres
psql (15.0)
Type "help" for help.

postgres=#
```

### Create a database

จากนั้นพิมพ์ SQL `CREATE DATABASE mypolls;` เพื่อทำการสร้าง database (อย่าลืม semicolon ;)

จากนั้นติดตั้ง VS CODE extension ชื่อ `PostgreSQL` by Weijan Chen เพื่อใช้ในการจัดการฐานข้อมูลผ่าน UI

ทำการตั้งค่า connection กรอกข้อมูลดังนี้

```bash
Name: mypolls
Host: 127.0.0.1
Username: your postgres username
Password: your postgres password
Port: 5432
```

## Migration

## Create a migrate python script

ทำการสั่ง `makemigrations` เพื่อสร้างไฟล์ migration ซึ่ง Django จะทำการ generate code สำหรับที่จะใช้นำไปสร้าง แก้ไข ลบ table ใน database โดยยึดจาก class models ที่เรากำหนดในไฟล์ `polls/models.py`

```bash
> python manage.py makemigrations polls
```

จะเห็นไฟล์ `polls/migrations/0001_initial.py` จะถูกสร้างขึ้นมาโดย Django

## Migrating a database

ทำการ migrate เพื่อสร้าง table ใน database `mypolls`

```bash
> python manage.py migrate polls
# Operations to perform:
#   Apply all migrations: polls
# Running migrations:
#  Applying polls.0001_initial... OK
```

# Models

เรามาสร้าง models กัน โดยใน app polls ของเราซึ่งมี 2 models ได้แก่ `Question` and `Choice` โดยเพิ่ม code ด้านล่างลงในไฟล์ `polls/models.py`

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

แต่ละ model class จะถูกนำไปสร้างเป็น table ใน database และแต่ละ field จะเป็น column ใน table โดยจะเห็นว่าเราได้ทำการกำหนด ประเภทของข้อมูลใน field เช่น CharField คือ field สำหรับบันทึกข้อมูล characters หรือ IntegerField คือ field สำหรับบันทึกข้อมูล integer

# Django Shell

เรามาลองเล่นกับ models ที่เราสร้างด้วย API ของ Django ใน Python shell กัน

```python
> python manage.py shell
```

# Misc

Drop all tables

```sql
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

# And then
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
```