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

```
python3 -m venv myvenv
```

In order to activate the environment:

```
source myvenv/bin/activate.fish
```

(Note that for bash you would just type `source myvenv/bin/activate` and then press tab for the right file name)

## Virtual Environment (venv)

In python, venv is a bit like doing Bundle Exec Rake in Ruby. It wraps up all your dependencies and things that you need to run your project in python.

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
