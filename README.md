# Credit_processing_for_Filed

# Overview

<h2>Main API </h2>

This project is created as a code excercise. It contains one method that processes payment requests like this:

  - CreditCardNumber (mandatory, string, it should be a valid credit card number)
  - CardHolder: (mandatory, string)
  - ExpirationDate (mandatory, DateTime, it cannot be in the past)
  - SecurityCode (optional, string, 3 digits)
  - Amount (mandatoy decimal, positive amount)
  
<h3>The Luhn Algorithm</h3> is implemented on a separate file to check for the validity of the credit card number.
  
The response of the method could be one of the following:

  - Payment is processed: 200 OK
  - The request is invalid: 400 bad request
  - Any error: 500 internal server error
  
It sends a request to any of these external "payment gateways" according to the amount of the transaction:
  - PremiumPaymentGateway
  - ExpensivePaymentGateway
  - CheapPaymentGateway
  
The API sends the request based on the following rules:
  a) If the amount to be paid is less than £20, use CheapPaymentGateway.
  b) If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
      Otherwise, retry only once with CheapPaymentGateway.
  c) If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
      in case payment does not get processed.

 <h2> Secondary API </h2>
 
 There is a separate API (Payment Gateways) that receives the requests from the main API. It checks whether the credit card number is valid 
 and has enough balance for the transaction and returns the appropriate response.
 
 The Payment Gateways API keeps a record of:
 - The name of the card holder
 - The card number
 - The available balance 

# Usage

A requirements.txt file is included.

<code> pip3 install -r requirements.txt </code> / <code> pip install -r requirements.txt </code>

Since there are two separate APIs, it is important to specify which port to run each of them.

The main API is written to run on <h3>port 5000</h3>

<pre> 
$ export FLASK_APP=main.py
$ flask run --host 0.0.0.0 --port 5000 
</pre>

The secondary API is written to run on <h3>port 5001 </h3>
This file is in the Payment Gateways folder.

<pre> 
$ export FLASK_APP=payment_gateways.py
$ flask run --host 0.0.0.0 --port 5001
</pre>


Two files are included for testing. 
One for multiple credentials stored in a dictionary within the file <code>test.py</code>, and one for manually entering credentials <code>test2.py</code>.



