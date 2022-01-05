# FarmGo

FarmGo is an e-commerce website that connects local producers directly with consumers for the Piedmont region in Italy.
It was a MSc group project where the aim was to learn how to create a website using Flask.

The design is a Model-View-Controller software pattern. 
The controller interacts with our flask package, the View is facilitated by the Jinja2 template and the Bootstrap framework,
and the model is created with SQLAlchemy.

In order to implement the web application, Python language was used in  the Flask framework environment. 
This decision has been made because Flask allows an easy implementation of database (SQL alchemy); 
includes useful extensions such as WTF forms, Bcrypt and Login. 
It also allows to create a built-in front-end with Jinja2 functionalities (HTML,CSS,JS).

The backend of the web application can be divided into three main categories:
• The Database – SQLAlchemy
• The Forms – WTForms Extension
• The Routes – Jinja2

As previously mentioned, the database was implemented with SQLAlchemy library in Flask which allows to define a table in the database, 
using the familiar object oriented approach, by defining classes.
The Flask-WTF extension was used to create the forms in our application. It is a simple integration with the WTForms library for python.
