# TWITTER

# Account app api with success response
===================================================================

api_url -> /api/account/people/
FOR SIGNING UP A USER
POST Request:
payload:{
    "phone_number":"8441000947",
    "user": {
		"username":"admin3",
		"password":"admin123",
		"email": "112223@123.com"
	}
}

reponse: {"token": "b799bf3359d47a12fc560c6f703b1a7edde1e7a9"}


===================================================================

API_URL -> api/account/login/
FOR LOGIN A USER
POST Request:
payload:{
	"username_or_email": "admin1",
	"password": "admin123"
}

reponse: {"token": "b799bf3359d47a12fc560c6f703b1a7edde1e7a9"}


===================================================================

API_URL -> api/account/logout/
FOR LOGOUT A USER
POST Request:
payload:{
	"username": "admin1",
}

reponse: {'success': 'logged out'}


===================================================================

API_URL -> api/account/people/3/
For getting a user profile
GET Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}
reponse: {
    "phone_number": "8441000947",
    "user_id": 2,
    "followed": [
        3
    ],
}

===================================================================

API_URL -> api/account/people/3/
For updating a user profile
PUT Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}
request payload: {
    "phone_number": "8441000947",
    "user_id": 2,
}

reponse: {
    "phone_number": "8441000947",
    "user_id": 2,
    "followed": [
        3
    ],
}

===================================================================

API_URL -> api/account/people/3/
For deleting a user profile
DELETE Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}

reponse: {"status": "Deleted"}

===================================================================


API_URL -> api/account/people/3/
FOR FOLLWING A NEW USER(id =5)
PUT Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}
request payload: {
    "followed": ["5"],
    "user_id": 2,
    "increase_follow" : true,
	"follower_change" : true,
}

reponse: {
    "phone_number": "8441000947",
    "user_id": 2,
    "followed": [
        3,4,5
    ],
}

===================================================================


API_URL -> api/account/people/3/
FOR UNFOLLWING A USER(id =5)
PUT Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}
request payload: {
    "followed": ["5"],
    "user_id": 2,
    "increase_follow" : false,
	"follower_change" : true,
}

reponse: {
    "phone_number": "8441000947",
    "user_id": 2,
    "followed": [
        3,4
    ],
}

===================================================================
===================================================================
===================================================================




# Tweet app api with success response


===================================================================


API_URL -> api/dashboard/homepage/
FOR SHOWING THE TWEETS ON HOME PAGE OF THE FOLLOWED USER IN RECENT SORTED ORDER
GET Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}

reponse: [
    {
        "msg": "ass",
        "people_id": 3,
        "like": 0,
        "title": "tackle"
    },
    {
        "msg": "asdasddas asdasd a. asdds",
        "people_id": 3,
        "like": 0,
        "title": "tackle"
    },
    {
        "msg": "asdasddas asdasd a. asdds",
        "people_id": 5,
        "like": 0,
        "title": "dadsas"
    },
    {
        "msg": "asdasddas asdasd a. asdds",
        "people_id": 6,
        "like": 0,
        "title": "dadsas"
    },
    {
        "msg": "asdasddas asdasd a. asdds",
        "people_id": 7,
        "like": 0,
        "title": "dadsas"
    },
    {
        "msg": "asdasddas asdasd a.",
        "people_id": 1,
        "like": 1,
        "title": "dads"
    }
]

===================================================================

API_URL -> api/dashboard/tweet/
FOR Creating a new tweet
GET Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}
request_payload: {
        "msg": "ass",
        "people_id": 2,
        "like": 0,
        "title": "tackle"
}
response:{
    "id": 6
}

===================================================================

API_URL -> api/dashboard/mytweets/
FOR GETTING ALL USER TWEET
GET Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}
response:[
    {
        "msg": "ass",
        "people_id": 2,
        "id": 6,
        "like": 0,
        "title": "tackle"
    },
    {
        "msg": "asdasddas asdasd a. asdds",
        "people_id": 2,
        "id": 5,
        "like": 0,
        "title": "tackle"
    },
    {
        "msg": "asdasddas asdasd a. asdds",
        "people_id": 2,
        "id": 3,
        "like": 0,
        "title": "dadsas"
    },
    {
        "msg": "asdasddas asdasd a. asdds",
        "people_id": 2,
        "id": 2,
        "like": 0,
        "title": "dadsas"
    }
]

===================================================================

API_URL -> api/dashboard/tweets/(?P<pk>[0-9]+)//
FOR Updating a particular tweet
PUT Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}
request_payload: {
        "people_id": 2,
        "like": 10,
        "title": "tackle"
}
response:{
        "msg": "sadsaa asddsa aass"
        "people_id": 2,
        "like": 10,
        "title": "tackle"
}

===================================================================

API_URL -> api/dashboard/tweets/(?P<pk>[0-9]+)//
FOR DELETING A TWEET
DELETE Request:
header: {
    "Content-Type": "application/json"
    "Authorization": "token 75e5639339a65e97dfe93a9a9e6b0d7e86c4c090"
}

response:{"status": "Deleted"}

===================================================================
