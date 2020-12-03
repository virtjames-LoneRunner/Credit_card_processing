# Credit_processing_for_Filed

# Overview

This project is created as a code excercise. It contains one method that processes payment requests like this:

  - CreditCardNumber (mandatory, string, it should be a valid credit card number)
  - CardHolder: (mandatory, string)
  - ExpirationDate (mandatory, DateTime, it cannot be in the past)
  - SecurityCode (optional, string, 3 digits)
  - Amount (mandatoy decimal, positive amount)
  
The response of the method could be one of the following:
  - Payment is processed: 200 OK
  - The request is invalid: 400 bad request
  - Any error: 500 internal server error
  
It sends a request to any of these external "payment gateways" according to the amount of the transaction:
  - PremiumPaymentGateway
  - ExpensivePaymentGateway
  - CheapPaymentGateway
 
 (There is a separate API (Payment Gateways) that receives the requests from the main API. It checks whether the credit card number is valid 
 and has enough balance for the transaction and returns the appropriate response.)

# Usage

A requirements.txt file is included.

<code> pip3 install -r requirements.txt </code> / <code> pip install -r requirements.txt </code>
