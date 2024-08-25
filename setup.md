This is a setup script, you just copy and paste.
But before that, ensure you're using venv and have node and docker installed.

Edit database configuration in the .env file

```bash
- Install Django on venv
pip install django
python -m django --version

pip install psycopg2
pip install psycopg2-binary

docker-compose -f docker-compose.yml up -d --build

pip install django-extensions ipython jupyter notebook
pip install ipython==8.25.0 jupyter_server==2.14.1 jupyterlab==4.2.2 jupyterlab_server==2.27.2
pip install notebook==6.5.7

```
