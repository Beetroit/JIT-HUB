from flask import Flask, request
import sys
import os

sys.path.insert(0, os.getcwd())
print(sys.path)
app = Flask("JIT HUB")
# from JIT_Dictionary import get_attributes


response = ""


@app.route("/ussd_dictionary", methods=["POST", "GET"])
def ussd_callback():
	global response
	data = request.values
	print(f"{data=}")
	session_id = request.values.get("sessionId", "")
	service_code = request.values.get("serviceCode", "")
	phone_number = request.values.get("phoneNumber", "")
	text = request.values.get("text", "default")
	print(f"{text=}")

	words = text.split("*")

	if text == "":
		response = """CON Welcome to JIT HUB, Kindly Pick a service"
	1. Dictionary Service
	2. Essential Service
	3. Emergency Service"""
		print(response)
	if text == "1":
		response = "CON Enter a word"
		# reply = get_attributes(text)
		# response = f"CON {reply}\n"
	if len(words)  == 2:
		return f"""CON Your words is {words[1]}"""
	if text == "1*1":
		accountNumber = "ACC1001"
		response = "END Your account number is " + accountNumber
	if text == "1*2":
		balance = "KES 10,000"
		response = "END Your balance is " + balance
	if text == "2":
		response = "END This is your phone number " + phone_number
	if len(words) > 2:
		return f"""END Your words is {words[2]}
			Thanks for using this service"""
	return response

@app.route('/events', methods=['GET','POST'])
def events():
	if request.method == "POST":
		data = request.values
		print(f"{data=}")
		with open('events.txt','w') as f:
			f.write(str(data))
	return "<h5> HI </h5>"



@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		return "OK"
	return "<h5> HI </h5>"


if __name__ == "__main__":
	app.run()
