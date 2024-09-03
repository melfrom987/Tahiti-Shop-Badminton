source myenv/bin/activate

pip install django

python manage.py runserver


python manage.py makemigrations
python manage.py migrate


python manage.py createsuperuser
