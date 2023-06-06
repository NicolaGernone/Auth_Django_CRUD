# STEP 1 Project Setup
For this task i choose an Hexagonal Architecture, because it is a good way to separate the business logic from the framework, and it is easy to test.
I set up the project with the following structure:
```bash
Auth_Django_CRUD # Django project
├── api # Django app
│   ├──application
│   │   ├──domain
│   │   │   ├── entities.py
│   │   │   ├── serializers.py
│   │   ├──services.py
│   ├──infrastructure
│   │   ├── views.py
│   │   ├── admin.py.py
│   │   ├── models.py
│   ├── migrations
│   ├── apps.py
│   ├── urls.py
├── app
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── manage.py
├── poetry.lock
├── pyproject.toml
├── docker-compose.yml
├── Docker
│   ├── Dockerfile
├── .gitignore
├── tests
│   ├── application
│   │   ├── domain
│   │   │   ├── factories.py
│   ├── infrastructure
│   │   ├── test_views.py
│   │   ├── test_models.py
```

#  STEP 2 Libraries used to authenticate with github

I used the library django-allauth to authenticate with github, it is a good library to authenticate with social networks, it is easy to use and it is well documented.

# STEP 3 Create user model and serializer

The models are referred to the user profile having as a external key the django user model and the user data.

# STEP 4 Create the views

I created the views to create, update, delete and list the user profile. i used ModelViewSet to create the views, it is a good way to create the views because it is easy to use.

# STEP 5 Create the tests

I created the tests to test the views and the domain, i used Django unit tests.

# STEP 6 Refactor the code to optimize the github api calls

After see some issue with the github login view i decide to optimize it with allauth api, so i call directly account/github/login to avoid endpoints problem.

Also i modify the entity to save the github data in the user profile, so i can avoid the github api calls in the views. Using Django AbstractUser i can save the github data in the user profile.

# STEP 7 Fix tests

I have to fix the tests because i change the user model, so i have to change the tests to use the new user model.
Same for the views, i have to change the views to use the new user model.


