from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

class BankModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    card_number = db.Column(db.String, nullable=False)
    balance = db.Column(db.Integer, nullable=False)

#db.create_all()


details = reqparse.RequestParser()
details.add_argument("card_number", type=str, help="Enter a valid Credit Card Number", required=True)
details.add_argument("card_holder", type=str, help="Enter the name of the Card Holder", required=True)
details.add_argument("card_expiration_date", type=str, help="Enter the Expiration Date", required=True)
details.add_argument("card_security_code", type=str, help="Enter your Security Code")
details.add_argument("transaction_amount", type=int, help="Name of the card holder", required=True)


successful_msg = {"message": "Payment is processed: "}, 200
error_msg = {"message": "The request is invalid: "}, 400 

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'card_number': fields.String,
    'balance': fields.Integer
}

class CheapPayment(Resource):
    #@marshal_with(resource_fields)
    
    def post(self):
        
        args = details.parse_args()
        amount = args["transaction_amount"]
        card_number = args["card_number"]

        account = BankModel.query.filter_by(card_number=card_number).first()
        account_balance = account.balance

        if amount > account_balance:
            return  error_msg
        else:
            return successful_msg

        

class ExpensivePayment(Resource):
    
    def post(self):
        account_balance = 499
        args = details.parse_args()
        amount = args["transaction_amount"]

        card_number = args["card_number"]

        account = BankModel.query.filter_by(card_number=card_number).first()
        account_balance = account.balance

        if amount > account_balance:
            return error_msg
        else:
            return successful_msg

        

class PremiumPayment(Resource):
    
    def post(self):
        account_balance = 1000
        args = details.parse_args()
        amount = args["transaction_amount"]

        card_number = args["card_number"]

        account = BankModel.query.filter_by(card_number=card_number).first()
        account_balance = account.balance

        if amount > account_balance:
            return error_msg
        else:
            return successful_msg

        

api.add_resource(CheapPayment, "/cheap")
api.add_resource(ExpensivePayment, "/expensive")
api.add_resource(PremiumPayment, "/premium")

if __name__ == "__main__":
    app.run(debug=True)