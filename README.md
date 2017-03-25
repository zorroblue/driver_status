# Driver status

This is an API for a real time driver availabiltiy system. This also includes a standalone website for checking too.

## Working:

There is an Android app  for drivers and it has a straightforward registration and log-in option. 
Once logged-in, the drivers can change the status in the app and is updated in the dashboard in realtime through API calls.

## Running:

To run the django  website in your local system, 

1. Clone the repository `git clone https://github.com/zorroblue/driver_status`
2. `cd driver_status`
3. Make migrations if any `python manage.py makemigrations`
4. Run migrations if any `python manage.py migrate`
5. Install the requirements `pip install -r requirements.txt` , preferrable in a virtual environment.
6. Run the server `python manage.py runserver`

It starts running in `localhost:8000/`






 
