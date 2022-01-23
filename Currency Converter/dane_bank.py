import requests
import datetime
import csv
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0].get('rates')

def get_codes():
    codes = []
    for data in rates:
        codes.append(data.get('code'))
    print(codes)
    return sorted(codes)

def rates_to_csv():
    fieldnames = ['currency', 'code', 'bid', 'ask']
    with open('rates.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rates)

rates_to_csv()
@app.route('/exchange', methods=["GET", "POST"])
def exchange():
    today = datetime.date.today()
    codes = get_codes()
    if request.method == "POST":
        if "formsubmit" in request.form:
            data = request.form 
            currency = data.get('code')
            amount = int(data.get('amount'))
            for rate in rates:
                if rate.get('code') == currency:
                    ask = rate.get('ask')
                    break
            cost = round(ask*amount,2)
            return f"{amount} {currency} = {cost} PLN"
        elif "formsubmit2" in request.form:
             data = request.form 
             currency = data.get('code')
             amountbid = int(data.get('amount'))
             for rate in rates:
                 if rate.get('code') == currency:
                     bid = rate.get('bid')
                     break
             cost = round(bid*amountbid,2)
             return f"{amountbid} {currency} = {cost} PLN"
    return render_template("form_rates.html", codes = codes, today=today)
