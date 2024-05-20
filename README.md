# FlaskApi Test

FlaskApi Test is a project featuring a Flask-based API with essential components such as main.py for database calls and routing, wsgi.py as an interface for route handling, and a Procfile for Gunicorn configuration on Heroku. The purpose of this project was to make a simulation of passengers boarding a plane, as to know and optimize the boarding process.

## API Folder:

- **main.py**: Contains the call to the database and defines the app's routing.

- **wsgi.py**: Acts as an "interface" for main.py, ensuring that the route definitions are not directly interacted with.

- **Procfile**: Allows Gunicorn to determine which file to use. This project is deployed on Heroku.

## Route:

The route is disabled.

https://bsalesapi.herokuapp.com/flights/#/passengers

Where # is the flight number, from 1 to 4.

## To run the API locally:

- Navigate to the api folder in the console and run: `pip install -r requirements.txt`
- In the console, run: `.\env\Scripts\Activate`
- Run the main file
