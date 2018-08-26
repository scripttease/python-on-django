# Following a Rails Tutorial with Python

Following a tutorial in a language you know and converting it as you go along into a language that you *don't* know, can, I am assured, be a good way to learn a new language.

I am following the [Hartle Rails Tutorial](https://www.railstutorial.org/book/toy_app#sec-planning_the_application) In Python and I am starting from chapter 2.1 because I covered installation in *../notes.md* following the DjangoGirls Guide. I may tidy this all up later...

## 2.1 Planning the application

Generate the application skeleton (and virtual environment which is required in Python and is similar to bundler I believe)

```sh
python3 -m venv venv

# note that for a standard bash shell, leave off .fish
source venv/bin/activate.fish

python3 -m pip install --upgrade pip

echo "Django~=2.0.6" >> requirements.txt

pip install -r requirements.txt

django-admin startproject ror_in_python_project .
```
**NB This last command scaffolds a project. See below for scaffolding an app within that**

### Static files path

**NB _settings.py_ is like a Gemfile**

At the end of the settings.py file add the following ine:

```py
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```


**This is the actual part where we scaffold the toy app**

```sh
python manage.py startapp toy_app
```

This whole project is in version control on Github. I'm going to leave out these steps. 

**BEFORE YOU COMMIT**
Go to *settings.py* and delete the Secret Key!!!
You can make it into an environment variable like so:

```py
SECRET_KEY = os.environ.get('SECRET')
```

However I will add deploying to Heroku but it is important to note that I will only deploy as if the route folder is *hartle-ror-in-python* whereas the version control (Git) in in the directory above that.

## Install [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

```python
brew install heroku/brew/heroku
```
 Log in:

```sh
heroku login
```
(you may need to create an account first)

## Usage of [Django-Heroku](https://github.com/heroku/django-heroku) 
At the bottom of *settings.py*:

```py
# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
```




