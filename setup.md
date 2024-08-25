This is a setup script, you just copy and paste.
But before that, ensure you're using venv and have node and docker installed.

Edit database configuration in the .env file

```bash
py -m venv myvenv
myvenv\Scripts\activate.bat

pip install django
python -m django --version

django-admin startproject PROJECT_NAME

pip install psycopg2
pip install psycopg2-binary

curl https://raw.githubusercontent.com/DrowningToast/django-setup-script/main/docker-compose.yml --output ./docker-compose.yml

docker-compose -f docker-compose.yml up -d --build

pip install django-extensions ipython jupyter notebook
pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2
pip install notebook==6.5.7

git clone git@github.com:aaapwn/Server-Side-Web-Development.git

```
