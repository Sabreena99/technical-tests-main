# Oddbox - Full-Stack Technical Test

The Oddbox Full-Stack technical test is designed to test your fundamental understanding of building and using the django framework to expose data for web applications. 

## Task

Your task is to model and store blog post data, expose the data via an API, and consume it on the frontend.

1. Create django model(s) to represent the blog data found in `data/posts.csv`. 
2. Write a loader to import the blog post data into your database.
3. Expose the blog posts via an api that supports pagination
4. Create a react component to fetch data from the api you created in step 3 and display in a looping carousel [mockup](mockup.png)

Please download this repository, add your changes, and upload them to a private GitHub repository. Invite [oddbox-team](https://github.com/oddbox-team) as a collaborator.

Please update this readme with instructions and any assumptions you may have made.

Please do not spend longer than 4 hours on the task - we are looking to understand your approach rather than your ability to build something production-ready in a morning!

## Getting Started

Some boilerplate has been created to help you get started, including django and django-admin for the backend, and create react app on the frontend. It requires [docker](https://www.docker.com/).

Feel free to use the boilerplate or to create your own.

```
> docker-compose run backend python manage.py migrate
```

Will create the database `src/backend/db.sqlite3`.

```
> docker-compose run backend python manage.py createsuperuser
```

To create a superuser for django-admin

```
> docker-compose up
```

Frontend:  http://localhost:3000
Backend:  http://localhost:8000
Django Admin:  http://localhost:8000/admin



## Instructions
1. Create virtual environment and activate it
2. cd into technical-tests-main/full-stack/src/backend
3. Install django rest framework and pillow(to use ImageField for models.py)
4. Run 'python manage.py runserver' and open link http://127.0.0.1:8000/blog/upload_data/

## Assumptions
1. Approach explained
The first thought that came to my mind when reading the task is that I don't want to upload csv and
save it to the server without validation and save the data to django model.

So my approach was to do the validation and insert data into model.
For this reason, a serializer is also created

2. Initially, updated the class Post (in blog/models.py) with all the fields from csv.
A PostViewSet is created in blog/views.py and a POST endpoint upload_data is created that supports pagination.
A PostSerializer class is also created in blog/serializers.py

3. INSTALLED_APPS in api/settings.py is updated to include rest_framework. Also default pagination settings is aded to the end of the file.

4. api/urls.py is updated to include url path for the new endpoint created.
The url path we are interested is '/blog/upload_data/'

5. POST method upload_data in blog/views.py explained:
Here, I take the file and read it using csv.DictReader and convert it into a list.
And pass this data to serializer and check if it is valid.
Then iterate over serializer data. Instead of uploading all the data in the for loop and hitting database every time, 
I have done it using bulk create. For this, a post_list is created and is appended with all the fields of model Post and the bulk create is done.


## Notes

...
