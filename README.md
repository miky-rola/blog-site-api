# BLOG API

## BLOG API with django

## Set up environment and run

1. Make sure Python 3.9 and virtualenv are already installed.

2. Clone the repo and configure the virtual environment:

`$ python -m venv env`

`$ source env/bin/activate for mac or env\scripts\activate for windows`

`$ pip install -r requirements.txt`


3. Set up environment variables. Examples exist in `.env.sample`:

`cp .env.sample .env`

4. Edit .env to reflect your local environment settings and export them to your terminal

`(env) $ source .env `

5. Run the initial migrations, build the database, create user and run project

`(env) $ python manage.py migrate`

`(env) $ python manage.py createsuperuser`

`(env) $ python manage.py runserver`

## Contribution
1. Create a new branch off the main branch.
2. Make your changes.
3. Push the new branch to github and create a PR to the main branch
