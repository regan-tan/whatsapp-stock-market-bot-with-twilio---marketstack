from flask import Flask
from flask import request
from twilio.rest import Client
import os
from marketstack import get_stock_price
app = Flask(__name__)

ACCOUNT_ID = os.environ.get('TWILIO_ACCOUNT')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
client = Client(ACCOUNT_ID, TWILIO_TOKEN)
TWILIO_NUMBER = 'whatsapp:+14155238886'

def process_msg(msg):
    response = ""
    if msg == "hi":
        response = "Hello, welcome to the stock market chatbot!"
        response += "Type sym:<stock_symbol> to get the latest stock price"
    elif 'sym:' in msg:
        data = msg.split(":")
        stock_symbol = data[1]
        stock_price = get_stock_price(stock_symbol)
        last_price = stock_price.get("last_price", "N/A")
        last_price_str = str(last_price)
        response = "The stock price of" + stock_symbol + " is " + last_price_str
    else: 
        response = "Please type hi to get started"
    return response

def send_msg(msg, recipient):
    client.messages.create(
        from_=TWILIO_NUMBER,
        body=msg,
        to = recipient
    )

@app.route("/webhook", methods=["POST"])
def webhook():
    f = request.form
    msg = f['Body']
    sender = f['From']
    response = process_msg(msg)
    send_msg(response, sender)
    return {
        "OK", 200
    }
