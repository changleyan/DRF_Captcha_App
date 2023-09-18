# Django REST Skeleton

**A Django REST framework project template for quickly bootstraping REST APIs**

---

This is an opinionated [Django][django] project skeleton based on:

- [Django REST framework][django-rest-framework]
- Configuration based on database URLs and configuration files
- Documentation with [Swagger][swagger]
- Authentication with OAuth2 [OAuth2][oaut2]
- Different database to store logs [Multiple_databases][multiple_databases]

---

## Getting Started

1. Clone the repo from GitHub
1. Delete the `.git` folder
1. Remove/add anything as you see fit
1. Initialize as a new git repository for your own project
1. Change database connection settings `config.run_mode.[dev_mode | prod_mode].DATABASES`
1. Install dependencies on your environment with the command `pip install -r .\requirements\all.txt `
1. Run the migrations with the command `python manage.py migrate`
1. Create superuser with the command `python manage.py createsuperuser`
1. Run the project using `python manage.py runserver` and you should see the default
   success page provided by Django at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
1. Access the Django admin and create an application for OAuth2 authentication and configure as shown in the following screenshot [OAuth2_Configuration][OAuth2_Configuration]. Important to copy the Client_id and the Secret_id

## Project layout

## Project Tree

```bash
.
├── apps
│   └── core # A django rest app
│       ├── api
│       │   ├── v1
│       │   │   ├── example_component
│       │   │   │   ├── __init__.py
│       │   │   │   ├── UserPermissions.py
│       │   │   │   ├── UserSerializer.py
│       │   │   │   └── UserViewSet.py
│       │   │   ├── __init__.py
│       │   │   ├── tests.py
│       │   │   └── urls.py
│       │   └── __init__.py
│       ├── models
│       │   └── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── tasks.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── common
│   ├── db
│   │   ├── __init__.py
│   │   └── ApiDBRouter.py
│   ├── middleware
│   │   ├── __init__.py
│   │   └── DisableCSRFMiddleware.py
│   ├── oauth2
│   │   ├── __init__.py
│   │   └── urls.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── utils.py
│   ├── __init__.py
│   └── generics.py
├── config
│   ├── run_mode
│   │   ├── __init__.py
│   │   ├── dev_mode.py
│   │   └── prod_mode.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── logs
│   ├── api.file.error.log
│   └── api.file.log
├── requirements
│   ├── all.txt
│   ├── deploy.txt
│   ├── dev.txt
│   ├── optional.txt
│   ├── required.txt
│   └── testing.txt
├── static
│   └── media
│       └── Configuracion de aplicacion de OAuth2.png
├── .gitignore
├── manage.py
└── README.md

```

2023, Leyan Chang
