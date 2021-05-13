# Ghana Regions Names Api

This api is used to get the list of regions in ghana

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

**Prerequisites**

```
Check requirements.txt for packages to install
```

**Installations for mac and linux users**

```
First clone the repository from Github and switch to the project directory
```

* git clone `https://github.com/Victorspy-web/ghana_regions_api`


```
Open terminal and install pipenv for your project
```

`
You can use any other way of creating a virtual env if you are familiar with venvs
`

* sudo apt install pipenv

```
Install Django, activate and migrate project
```

* pipenv install django==3.2 . `Dont forget the space and dot at the end!`
* pipenv shell
* pip install Pillow
* python manage.py makemigrations
* python manage.py migrate


```
Create django superuser
```

* python manage.py createsuperuser
    * Fill in the fields to create a superuser `Passwords are invisble`


```
You can now run the development server
```

* python manage.py runserver
