import requests

import time

BASE = "http://127.0.0.1:5000/"

credentials = [{"card_number": "378282246310005", "card_holder": "James", 
                "card_expiration_date": "05-21", "card_security_code": "645", 
                "transaction_amount": 9},

                {"card_number": "371449635398431", "card_holder": "Anthony (Exceeded Balance)",
                "card_expiration_date": "01-25", "card_security_code": "897",
                "transaction_amount": 409},

                {"card_number": "378734493671000", "card_holder": "Lester (Exceeded Balance)",
                "card_expiration_date": "06-23", "card_security_code": "097",
                "transaction_amount": 12000},

                {"card_number": "4222431287594", "card_holder": "Hazel",
                "card_expiration_date": "10-21", "card_security_code": "453",
                "transaction_amount": 30},

                {"card_number": "222100000000000A", "card_holder": "Lee (Added \"A\" to card number )",
                "card_expiration_date": "01-23", "card_security_code": "007",
                "transaction_amount": 12},

                {"card_number": "2223000048400011", "card_holder": "Steve (Invalid Card)",
                "card_expiration_date": "11-23", "card_security_code": "009",
                "transaction_amount": 1232},

                {"card_number": "378734984032196", "card_holder": "Lester (Invalid Card)",
                "card_expiration_date": "07-24", "card_security_code": "997",
                "transaction_amount": 800},

                {"card_number": "2223016768739313", "card_holder": "Scarlette (Invalid Card)",
                "card_expiration_date": "09-20", "card_security_code": "427",
                "transaction_amount": 800},

                {"card_number": "5555555555554444", "card_holder": "Jeremy",
                "card_expiration_date": "05-19", "card_security_code": "107",
                "transaction_amount": 9},

                {"card_number": "4111111111111111", "card_holder": "Bruce",
                "card_expiration_date": "05-22", "card_security_code": "187",
                "transaction_amount": 4000},

                {"card_number": "4012888888881881", "card_holder": "Jake",
                "card_expiration_date": "04-25", "card_security_code": "287",
                "transaction_amount": 12},

                {"card_number": "4222222222222", "card_holder": "Jeremy",
                "card_expiration_date": "05-22", "card_security_code": "987",
                "transaction_amount": 4500},

                {"card_number": "5105105105105100", "card_holder": "Fin",
                "card_expiration_date": "05-22", "card_security_code": "897",
                "transaction_amount": 1234},

                {"card_number": "5105105105105100", "card_holder": "Fin (Exceeded Balance)",
                "card_expiration_date": "08-21", "card_security_code": "906",
                "transaction_amount": 2100},
                ]
                

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
        time.sleep(3)


checkout(credentials)