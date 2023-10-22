from flask import Flask, request
import sys
import os

from JIT_Dictionary.main import get_entries

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
		return response
	if text == "1":
		response = "CON Enter a word"
		# reply = get_attributes(text)
		# response = f"CON {reply}\n"
		return response
	if len(words)  == 2:
		entries = get_entries(words[1])
		results=[{'POS':i[0], 'def.':i[1], 'usage':i[2], 'similar':', '.join(eval(i[3])), 'opposite':', '.join(eval(i[4]))} for i in [str(i).split('\n') for i in entries[0].meanings]]
		return f"""CON Your word is {words[1]}
		{results[0]}
		{results[1]}
		
		1. Get all meanings as sms (pro)
		2. Quit
		"""
	if len(words) == 3:
		print(words)
		if isinstance(eval(words[0]), int) and isinstance(eval(words[1]), 'str') and eval(words[2]) ==1:
			return f"""END Your results will arrive shortly
				Thank you for using USSDICT (JITHUB)"""
		elif isinstance(eval(words[0]), int) and isinstance(eval(words[1]), 'str') and eval(words[2]) ==2:
			return f"""END Thank you for using USSDICT (JITHUB)"""
	return f"""END Try again with a new query"""

@app.route('/events', methods=['GET','POST'])
def events():
	if request.method == "POST":
		data = request.values
		print(f"{data=}")
		with open('events.txt','+a') as f:
			f.write(str(data))
	return "<h5> HI </h5>"



@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		return "OK"
	return "<h5> HI </h5>"


if __name__ == "__main__":
	app.run()
