# FlaskApi Test

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
