from flask import Flask, request
import sys
import os
sys.path.insert(0, os.getcwd())
print(sys.path)
app = Flask('JIT HUB')
# from JIT_Dictionary import get_attributes


response = ""

@app.route('/ussd_dictionary', methods=['POST', 'GET'])
def ussd_callback():
  global response
  data = request.values
  print(f"{data=}")
  session_id = request.values.get("sessionId", '')
  service_code = request.values.get("serviceCode", '')
  phone_number = request.values.get("phoneNumber", '')
  text = request.values.get("text", "default")
  print(f"{text=}")
  if text == '':
    response  = """CON Welcome to JIT HUB, Kindly Pick a service"
    1. Dictionary Service
    2. Essential Service
    3. Emergency Service"""
    print(response)
  elif text == '1':
    response = 'CON Enter a word'
    # reply = get_attributes(text)
    # response = f"CON {reply}\n"
    
  elif text == '1*1':
    accountNumber = "ACC1001"
    response = "END Your account number is " + accountNumber
  elif text == '1*2':
    balance  = "KES 10,000"
    response = "END Your balance is " + balance
  elif text == '2':
    response = "END This is your phone number " + phone_number
  return response



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       return 'OK'
    return '<h5> HI </h5>'
if __name__ == '__main__':
    app.run()