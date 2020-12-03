from flask import Flask
from flask_restful import Api, Resource, reqparse
import requests


from credit_test import check_card, parse_number
import expiration_test

import time

app = Flask(__name__)
api = Api(app)
 

payment_details_args = reqparse.RequestParser()
payment_details_args.add_argument("card_number", type=str, help="Enter a valid Credit Card Number", required=True)
payment_details_args.add_argument("card_holder", type=str, help="Enter the name of the Card Holder", required=True)
payment_details_args.add_argument("card_expiration_date", type=str, help="Enter the Expiration Date", required=True)
payment_details_args.add_argument("card_security_code", type=str, help="Enter your Security Code")
payment_details_args.add_argument("transaction_amount", type=int, help="Name of the card holder", required=True)

def check_expiration(validity, expiration_date):
    if validity != "INVALID":
        if expiration_test.check_validity(expiration_date):
            return True

        elif expiration_test.check_validity(expiration_date) == False:
            return False

    else:
        return False

def send_payment(args):

    BASE = "http://127.0.0.1:5001/"

    amount = args["transaction_amount"]

    if amount < 20:
        #Use CheapPaymentGateway
        response = requests.post(BASE + "cheap", args)
        print(1)
        return response

        

    elif amount > 20 and amount <= 500:
        # Use Expensive if available otherwise retry once with CheapPaymentGateway
        response = requests.post(BASE + "expensive", args)
        tries = 0
        print(2)
        while response.status_code != 200:
            while  tries < 1:
                response = requests.post(BASE + "expensive", args)
                tries += 1
                time.sleep(3)
            break

        return response
        

    elif amount > 500:
        # User Premium and retry 3 times
        response = requests.post(BASE + "premium", args)
        tries = 0
        print(3)
        while response.status_code != 200:
            while tries < 3:
                response = requests.post(BASE + "premium", args)
                tries += 1
                time.sleep(3)
            break

        
        return response
        




class ProcessPayment(Resource):
    def post(self):
        
        args = payment_details_args.parse_args()
        card_number = args["card_number"]
        expiration_date = args["card_expiration_date"]

        card = parse_number(card_number)
        validity = check_card(card)

        card_status = check_expiration(validity, expiration_date)

        if validity != "INVALID" and card_status == True:

            status = send_payment(args)
            return status.json(), status.status_code
        
        else:
            status = {"message": "The request in invalid: "}, 400
            return status
        


        


api.add_resource(ProcessPayment, "/pay")

if __name__ == "__main__":
    app.run(debug=True)