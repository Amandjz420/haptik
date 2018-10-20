# function solution
This folder contains solution to question 1 and question 3
first install requirement.txt in function_solution folder

then run file to see output
python activeuser.py
python wordformer.py

# twitter
For building the backend of Twitter, i used Django a python frameworks.
As for the sites like twitter or facebook. the developer has to process large number of data for which
python provides good library, be it for data crunching or using machine learning.
Also django is very scalable tool with easy integration for db or any workers.

I am using PostgressDb for having access of ArrayField

# DB Schema
There are two tables holding all the data

1.) People model:

user - onetoonefield with User django provides
phone_number - is a string that can contain mar 13 digits
birth_date - is a date field
followed - An arrayfield for containing the other people ids for following them
created - date field for creation of object
modified - date field for modification of object

2.) Tweet model:

title - is a string that has title of any tweet
msg - is a string that is content of any tweet
like - number of like for a post
people - foreign key with the model People
created - date field for creation of object
modified - date field for modification of object



API's:

POST - /api/account/people/ FOR SIGNING UP A PERSON
POST - /api/account/login/ FOR LOGIN A USER POST
POST - /api/account/logout/ FOR LOGOUT A USER POST

GET - /api/account/people/3/ FOR GETTING A PERSON PROFILE
PUT - /api/account/people/3/ For updating a user profile,
            Same api with different payload can be used to follow/unfollow another person

DELETE - /api/account/people/3/ For deleting a user profile

GET - /api/dashboard/homepage/ FOR SHOWING THE TWEETS ON HOME PAGE OF THE FOLLOWED USER IN RECENT SORTED ORDER
POST - /api/dashboard/tweets/ FOR Creating a new tweet
GET - /api/dashboard/mytweets/ FOR GETTING MY TWEET
PUT - /api/dashboard/tweets/(?P[0-9]+)/ FOR Updating a particular tweet
DELETE - /api/dashboard/tweets/(?P[0-9]+)/ FOR DELETING A TWEET DELETE


This backend server cant take too many request simultaneously,
we will have to use nginx like service to get the requests from users
Also the array field for storing following will create a problem and very heavy sql query as data grows



For starting the twitter dajngo service
go to twitter directory
run command
- pip install -r requirement.txt
- install postgres on the system
- python manage.py migrate
- python manage.py runserver
- Keep populating the data using the api documentation in twitter's READme


