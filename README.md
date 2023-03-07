# Socialbook 

Welcome to my first 'serious' app, which is a social networking service that resembles 'Facebook' to some extent.
Although there's still plenty of work to be done on it, unfortunately, I haven't had much time recently to improve
its appearance and functionality. Despite that, the app has all the necessary functionalities to work, such as:

>- creating an account and logging in to it
>- adding posts on the timeline
>- dropping comments under posts
>- hitting a 'like' button and unliking it
>- adding and removing friends from a list of all users
>- changing account's personal data
>- playing a JavaScript based simple game

Further development of this app is to be continued...

- I added this project here with only one main commit and push as I was still learning and not very familiar with GitHub at the time.

## Prerequisites
- Python 3.9 or higher
## Installation
1. Clone the repository.

2. Create a virtual environment and activate it:
```bash
python3 -m venv env
source env/bin/activate
```
3. Install the dependencies:
```bash
pip install -r requirements.txt
```
4. Configure your own database in the settings.py file and then run the command:
```bash
python3 manage.py migrate
```
5. Create a superuser:
```bash
python3 manage.py createsuperuser
```
6. Run the development server:
```bash
python3 manage.py runserver
```
## Technology Used
- Python/Django
- Vanilla JS
- PostgreSQL

## Visuals
Photos of this project are available [here](https://photos.app.goo.gl/rbEup1xe6gA5TGyGA
"Google Photos album").
