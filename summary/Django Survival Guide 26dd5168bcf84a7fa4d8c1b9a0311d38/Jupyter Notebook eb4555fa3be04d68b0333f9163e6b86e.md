# Jupyter Notebook

การใช้งาน Django ใน Jupyter Notebook สามารถทำตามขั้นตอนดังนี้

# 1. ติดตั้ง virtualenv โดยกำหนด version ของภาษา python ดั่งนี้

สำหรับ Windows

```bash
> py -m venv myvenv
```

สำหรับ MAC OS

```bash
> python3 -m venv myvenv4
```

activate และติดตั้ง Django และ psycopg2

```bash
> pip install django psycopg2-binary
```

# 2. ติดตั้ง Django

[Setting up Django](Setting%20up%20Django%20f6d767bdf9e94c858bcb225b684e9889.md)

# 3.ติดตั้ง `django-extensions` และ `jupyter notebook` ด้วยคำสั่ง

```bash
> pip install django-extensions ipython jupyter notebook   
```

# 4. จากนั้นให้แก้ไข version ของ package ภายใน jupyter และ notebook

```bash
> pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2
```

แก้ไข version notebook

```bash
> pip install notebook==6.5.6
```

หากติดตั้ง หรือ run jupyter ไม่ได้ให้ลองเปลี่ยน notebook version ดังนี้ `6.5.7` (Windows)

# 5.  จากนั้นสร้าง directory ชื่อ `notebooks`

```bash
mkdir notebooks
```

# 6. เพิ่ม `django-extensions` ใน INSTALLED_APPS ในไฟล์ settings.py

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "django_extensions",
    "blogs",
]
```

# 7. ทำการ start Jupyter Notebook server ด้วย command

```bash
python manage.py shell_plus --notebook
```

ซึ่งจะเปิด Jupyter Notebook ขึ้นมาใน Web Browser

# 8. เข้าไปที่ folder `notebooks`

![Untitled](Jupyter%20Notebook%20eb4555fa3be04d68b0333f9163e6b86e/Untitled.png)

สร้าง ไฟล์ ipynb สำหรับใช้กับ project django

![Untitled](Jupyter%20Notebook%20eb4555fa3be04d68b0333f9163e6b86e/Untitled%201.png)

# 9. จากนั้นใน Cell แรกของไฟล์ Notebook เพิ่ม code นี้ลงไป

```python
import os
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
```

![Untitled](Jupyter%20Notebook%20eb4555fa3be04d68b0333f9163e6b86e/Untitled%202.png)

# 10. สามารถทำการ import models และ query ข้อมูลโดยใช้ API ของ Django ได้เลย

```python
from blogs.models import Blog

for blog in Blog.objects.all():
    print(blog)
```