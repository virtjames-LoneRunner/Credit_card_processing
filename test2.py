import requests

import time

BASE = "http://127.0.0.1:5000/"

def checkout(credentials):

    for account in credentials:

        response = requests.post(BASE + "pay", account)

        status = ''

        if response.status_code == 200:
            status = 'OK'

        elif response.status_code == 400:
            status = 'bad request'

        else:
            status = 'internal server error'


        print("Processing transactions for " + account["card_holder"] +" with amount: " + str(account["transaction_amount"]))

        print(response.json()["message"] , response.status_code, status)

        print("Waiting...\n")
        time.sleep(5)

print("Examples of Acceptable Accounts")
print("""
    card_number : 378282246310005
    card_holder : James 
    card_expiration_date : 05-21
    card_security_code : 645 
    transaction_amount: 9


    card_number : 5555555555554444 
    card_holder : Jeremy
    card_expiration_date : 05-19 
    card_security_code : 107
    transaction_amount : 17


    card_number : 4222431287594
    card_holder : Hazel
    card_expiration_date : 10-21
    card_security_code: 453
    transaction_amount: 11
""")

card_number = input("Enter your card Number: ")
card_holder = input("Enter the card holder's name: ")
card_expiration_date = input("Enter the card's expiration date: ")
card_security_code = input("Enter security code(optional): ")
transaction_amount = input("Enter transaction amount: ")

credentials = [{"card_number": card_number, "card_holder": card_holder, 
                "card_expiration_date": card_expiration_date, "card_security_code": card_security_code, 
                "transaction_amount": transaction_amount}]
checkout(credentials)