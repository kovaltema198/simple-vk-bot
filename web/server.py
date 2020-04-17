from flask import Flask, request
from config import confirmation_token, sercet_key
import json

class WebServer:

	handlers = {}

	def __init__(self, flask):
		self.flask = flask

	def on(self, eventType):
		def wrapper(func):
			if self.handlers.get(eventType):
				self.handlers[eventType].append(func)
			else:
				self.handlers[eventType] = [func]
			return func
		return wrapper

app = WebServer(Flask(__name__))

@app.flask.route('/', methods=["POST"])
def h():
	try:
		data = json.loads(request.data)

		if (data.get("secret") != sercet_key):
			return "Error 404, page not found", 404

		if (data.get("type") == "confirmation"):
			return confirmation_token

		if app.handlers.get(data["type"]):
			for handler in app.handlers[data["type"]]:
				handler(data)

		return "ok"
	except Exception as e:
		print(e)
		return "error", 500