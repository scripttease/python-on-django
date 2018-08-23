## 1.2.2 Installing Python

See resources from (https://tutorial.djangogirls.org/en/installation/ [https://tutorial.djangogirls.org/en/installation/] 

- don't forget to open the file called 'install certificates.command' 
This runs a script from the terminal to install the required SSL certificates

- Next I ran the 'Update Shell Profile.command' which runs this:

```
alice_dee ~ $ /Applications/Python\ 3.6/Update\ Shell\ Profile.command ; exit;
This script will update your shell profile when the 'bin' directory
of python is not early enough of the PATH of your shell.
These changes will be effective only in shell windows that you open
after running this script.
Sorry, I don't know how to patch fish shells
```
OK this was ... all wrong and I'm not sure how to undo it BUT

to get python3 and ipythin at usr/bin/local which is where you generally want this stuff do this:

```
brew install python3
brew install ipython

```

Then following the DjangoGirls tutorial I created a virtual environment as follows inside my project folder:

## Virtual Environment (venv)

In python, venv is a bit like doing Bundle Exec Rake in Ruby. It wraps up all your dependencies and things that you need to run your project in python.


```
python3 -m venv myvenv
```

In order to activate the environment:

```
source myvenv/bin/activate.fish
```

(Note that for bash you would just type `source myvenv/bin/activate` and then press tab for the right file name)


## Installing Django

Now from the myvenv prompt you can install Django, using the latest version of pip (python install, like gem libraries)


```
python3 -m pip install --upgrade pip
```

You want to keep track of all the files installed by pip for this project so you need to manually create a requirements.txt file

```
touch requirements.txt
```
Edit the file to include the text

> Django~=2.0.6


now run 
```
pip install -r requirements.txt
```

## Python interpreter

```
python3
```
Example:

```
>>> 2 + 2
4
>>>
```

##Python Files

Exit the interpreter using Ctrl D or type 'exit'

From the venv prompt:
```
touch hello_world.py
```
the .py extension is a python executable file

To run the file use:

```
python3 hello_world.py
```

So long as you are in venv, this will also work:
```
python hello_world.py
```

This is because the venv handles the versions for you.

## Fuctions

```py
def hi():
    print("hi there")

hi()
```
## For other examples see:

hello_world.py and
recursion.py

## Create Djanjo project framework:

```sh
django-admin startproject mysite .
```

The following file tree will be created in the current working directory:

├───manage.py
├───mysite
│        settings.py
│        urls.py
│        wsgi.py
│        __init__.py
└───requirements.txt

(which also includes examples files as well as a myvenv folder)

### Static files path
At the end of the settings.py file add the following ine:

```py
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
### Hosts
When DEBUG is True and ALLOWED_HOSTS is empty, the host is validated against ['localhost', '127.0.0.1', '[::1]']. This won't match our hostname on PythonAnywhere once we deploy our application so we will change the following setting:

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

## Set up database

Database settings can be found in the mysite/settings.py file. In order to set up the sqlite database that comes with django use:

```sh
python manage.py migrate
```

## Start web server

```sh
python manage.py runserver
```

Note that this will run in the terminal so to get a new myenv promt, navigate to the directory in a new terminal tab or window and:
```
source myvenv/bin/activate [tab for appropriate extension]
```

### Check that mysite is being hosted locally 

Navigate to localhost:8000 in your browser

## Django Models

bject oriented programming is the idea that, rather than just procedural (a sequence of instructions as it were) programs can be models of ideas and concepts

These models are made up of objects that have attributes or properties to describe them, and have actions or methods that allow them to interact with each other and the world

This tutorial is about making a blog. We can think of modelling a post as follows

> Post
> --------
> title
> text
> author
> created_date
> published_date
> publish()       # this is a method

Note that this kind of object modelled in Django, can be stored in a database (as there are likely to be lots of posts)

An object with methods and properties such as a post would usually be described in Pythin by a class

## Creating an application

A project might have many parts to it, in programming these are referred to often as applications. To make a blog app in our project folder:

```sh
python manage.py startapp blog
```

The project folder directory should now look like this:

> project-folder
> ├── blog
> │   ├── __init__.py
> │   ├── admin.py
> │   ├── apps.py
> │   ├── migrations
> │   │   └── __init__.py
> │   ├── models.py
> │   ├── tests.py
> │   └── views.py
> ├── db.sqlite3
> ├── manage.py
> └── mysite
>     ├── __init__.py
>     ├── settings.py
>     ├── urls.py
>     └── wsgi.py

To tell Django to find and use this app, we need to edit the mysite/settings.py file to include the last line 'blog' as shown below:

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

## models.py

Like the rails convention of model=view-controller, python has models too. These contain the objects that you are modelling and are defined/described by classes.

When modelling an object such as a post, that is going to be stored in a database, you also include the database field descriptors such as ForeignKey (which links it to other models), type of field (such as CharField (character field) and whether it can be black or null. This (in Ruby) is known as a schema and is NOT stored with the model. 

## Migrations

To crate a migration file from your model (which you can then edit for more complicated database shenanigans) run:

```sh
python manage.py makemigrations blog
```

This generates a migration file called something like 0001_initial.py. To add the model actually to the database run:

```sh
python manage.py migrate blog
```

## Registering Models

This is done in the blog/admin.py file:

```py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

## Create admin/superuser

```sh
python manage.py createsuperuser
```

## Securiyt and deployment

Can take local_settings out of version control and just commit settings with debug set to false and the secret key as an environment vatiable:

```py
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()
```
or 

```py
SECRET_KEY = os.environ['SECRET_KEY']
```
And debug set to false but to continue dev while being deployed is very frustrating like this I feel like there should be a much better way...

like to have a dev env and a prod env that you just switch to really easily/happens automativcally...

probably best to just use environment variables
In the meantime I have changed manage.py and wsgi.py settings.py references to local_settings.py which isn't in version control.

Debug is still set to True in the local_settings which is one of the things that would be good to have in a dev env but not prod...


/******** NB remember to change TZ to UTC +1********


## Registering Models with Admin

In order to use the GUI that Django provides for admins to let us add, edit etc objects in the database, we don't have to always use a shell like in Ruby - we can use the admin/superuser account but to do this the models need to be registered in *blog/admin/py*

```py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

## URL configuration

```py
"""mysite URL Configuration

[...]
"""
```
Anything elclosed in """ in py is a docstring
```py
from django.urls import path, include
from django.contrib import admin
```
These import from python librarie - we use 'include' below so we need to import it as it isn't in the std lib
```py
urlpatterns = [
    path('admin/', admin.site.urls),
]
```
In the py tuple above the first item is the string containing the part of the url ('' is the root, 'admin/' is home/admin/) the second item is location of the view (which contains the logic for making the template html which is rendered on the page) The syntax for directories here is that a '.' replaces what we would normally read as a '/' in a file directory so the admin views are in *admin/site/urls.py* which incidentally is part of the admin library imported above so you cant actually see it. To keep this url file tidy we will redirect to the urls.py file in the *blog* folder with the following line:

```py
    path('', include('blog.urls')),
```

And in *blog/urls.py* :
```py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```
The import path is the library used for easily importing files and then we import views from the current folder (which is what 'from .' means.

The tuple contains the url part, the name of the view function (although here the '.' isn't a subfolder, it is a definition inside the views.py file, and then 'name='post_list' which is to do with namespacing (see [https://docs.djangoproject.com/en/2.0/topics/http/urls/](https://docs.djangoproject.com/en/2.0/topics/http/urls/)

A minimal view could now be created in *blog/views.py* as follows:

```py
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
```

## Templates

The render library looks for templates in a directory names templates so the above instruction looks at *blog/templates/blog/post_list.html* for the template. 

## Interactive Shell/console

to query the database from the shell etc from the myenv prompt run:

```sh
python manage.py shell
```

## Dynamic data in templates

in *blog/views.py* add:

```py
from .models import Post

def post_list(request):

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {})
```

### Querysets 
 Under the def above we assign the variable posts using the Django ORM (Querysets) language. the '/_/_' is how you attach a method to a field in this synax ('lte' is less than or equal to, 'contains' is just 'contains' but note this is NOT the same filter as Pythin's filter it is just for queries.

Now in Django terminology we have created a queryset called 'posts'

This needs to be passed as a parameter in the render, so the last line becomes:

```
    return render(request, 'blog/post_list.html', {'posts': posts})
```

### Template tags and filters (built in django)

In order to include code and parts of models etc in your templates, including variables assigned in the views, including ways to filter and add line breaks etc. See docs:
[https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#block](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#block)

## Static files (css etc)

> myproject
> ├── blog
> │   ├── migrations
> │   ├── static
> │   │   └── css
> │   │       └──blog.css
> │   │   
> │   └── templates
> └── mysite

Make the *static* folder shown above is where in your directory you should keep the static files such as css files as shown.

To read these from the generated html include the following in the *blog/post_list.html* file at the beginning:
```html
{% load static %}
```
And this line at the end of the head tag
```html
<link rel="stylesheet" href="{% static 'css/blog.css' %}">
```
Note it is loaded AFTER the css files so that it overwrites them so you have bootstrap PLUS your own css...

## Template extending

placing a file called base.html in your *templates/blog* directory means that you can use the same head and headers footer, titles etc in all your templates without repeating the code. Then hte page-specific code can be called using the following code in the body tag of the base.html file:

```html
<body>
    <div class="page-header">
        <h1><a href="/">Python Blog</a></h1>
    </div>
    <div class="content container">
        <div class="row">
            <div class="col-md-8">
            {% block content %}
            {% endblock %}
            </div>
        </div>
    </div>
</body>
```

it is the block endblockinserted Python code that is important here. To link the page specific html to the base html start the pot_list.html filr with :

```html
{% extends 'blog/base.html' %}
```
And surround the page specific html with Python inserted code block-endblock notation as shown (example of post_list.html file):


```html
{% extends 'blog/base.html' %}
{% block content %}
{% for post in posts %}
<div class="post">
    <div class="date">
        {{ post.published_date }}
    </div>
    <h1><a href="">{{ post.title }}</a></h1>
    <p>{{ post.text|linebreaksbr }}</p>
</div>
{% endfor %}
{% endblock %}
```

## Django template tag URLs and links to database objects

In order to link to a specific post (ie the first post) in our blog we could add a url to the href link on this line in post_list.html

```html
 <h1><a href="">{{ post.title }}</a></h1>
```
like so:
```html
<h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
```
This uses django's URL template tag, which has space seperated arguments, the first being a view, the second, third ... being optional arguments used in the url.

The `pk=post.pk` means that for each post ew will get a pk (primary key). This is an attribute for an object. We have defined post with the line `for post in posts` in the template, and posts is defined in our view BUT it is defined under post_list NOT post_detail... so we need to remember to define `post` in our view in the post_detail function/action/method as well as reusing the definition for Posts

The `post_detail`  in the above *href* means that we need a URL in *blog/urls.py* with `name=post_detail`: It should look like this

```python
    path('post/<int:pk>', views.post_detail, name='post_detail'),
```

The view title and name are straight forward but when it comes to the route or what we want the url to actually look like - well here we want `/post/1` or `post/2` or whatever number is appropriate and so we can use the primary key which is automatically assinged to make every entry unique even if all other fields are the same. You can make the primary key have a name OR a value if you like but if you don't, one is just assigned and it gies up numerically. In Rails and other frameworks the pk is often called the id.
This part `post/<int:pk>/` specifies a URL pattern:

* post/ just means that the URL should begin with the word post followed by a /. 
* `<int:pk>` – this part is trickier. It means that Django expects an integer value and will transfer it to a view as a variable called pk.

That means if you enter http://127.0.0.1:8000/post/5/ into your browser, Django will understand that you are looking for a view called post_detail and transfer the information that pk equals 5 to that view.

we don't have a view yet...

we know that the post detail definition needs to have two parameters now, the request, and the pk...

We can use Post.objects.get(pk=pk) (like doing Post.objects.get(pk=1) but with the variable we have passed to the view being the correct post number) to get the primary key but we need to catch the error when there is no post with the primary key specified.

Our view will have this included:

```py

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blog/post_detail.html', {'posts': posts})
```

Notice how we can rewrite `Post.objects.get(pk=pk)` as `get_object_or_404` with the *argument* as Post instead of having it as a method on Post. The secod argument is what the argument for `.objects.get` would have been.

In the views we can also import Django's nice 404 page:
```
from django.shortcuts import render, get_object_or_404
```


