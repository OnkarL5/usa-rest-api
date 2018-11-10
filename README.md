# REST api for registering and retrieving user data (Ready to deploy on Heroku)
python, flask, flask-RESTful, flask_jwt, SQLAlchemy

## User Database
username  
firstName  
lastName  
email  
phone  
profilePic  
pincode  
password  

## endpoints
to register: /api/register  
to retrieve user data: /api/user/<string: name>  

## HTTP status
200 - ok  
201 - insertion successful  
400 - insertion unsuccessful/bad request  
404 - not found  
