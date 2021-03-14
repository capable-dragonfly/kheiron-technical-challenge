# kheiron-technical-challenge
Code for the Kheiron take home technical challenge.

To install requirements: `pip install -r requirements.txt`

To run the service: `FLASK_APP={path to calculator_service.py} flask run`

Send requests to the service endpoint `/calculate` and provide the parameters `calculation` and `notation` (`infix` or `prefix`). 

Make sure the special characters in your calculation parameter are properly encoded. See `calculation_requests.http for two examples.
