# suade_ecommerce
A simple ecommerce mock-up website, done as a challenge. 


# Setup and use guide

- Clone the repository
- Create a virtual environment, for this challenge I used venv using the following command:
` py -m venv .\venv`

- Install the necessary python dependencies using once the virtual environment as been activated:
`pip install -r requirements.txt`

- After the installation is complete, create a .env file with the following content, the CONFIG_TYPE can be either 'development' or 'production' (only altering the debug flag):
FLASK_APP = app.py
CONFIG_TYPE = development


After creating the .env file, the database can be created running the python script in the data directory which will populate the relevant tables with the data provided in the csv files. Ensure the csv files are in the data/csv directory. :
`py -m .\data\models.py`

- Run the application using the following command:
flask run

- Navigate to the following URL: http://127.0.0.1:5000/data and populate a date parameter with a date string in the format YYYY-MM-DD.
Complete example:  http://127.0.0.1:5000/data?date=2019-09-10

See below image for the result.

# Potential Futrue To-DO's:
- Create a Docker image that would spin up an image of the app with the necessary dependencies
- Scalability:
    - Use rabbitmq for task queuing and celery for task dequeueing/handling
    - If the applications had more views and routes, create specific modules for main component using flask blueprinting
- Tests:
    Further expand testing the frontend specifically ensuring appropriate html responses



