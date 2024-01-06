# CMS

How to run
1. Install Django `pip3 install -r requirements.txt`
2. Create migrations if there are some changes in models.py `python3 manage.py makemigrations`
3. Apply migrations `python3 manage.py migrate`
4. Create superuser `python3 manage.py createsuperuser`
5. Run server `python3 manage.py runserver`


Admin site:
`http://127.0.0.1:8000/admin/`