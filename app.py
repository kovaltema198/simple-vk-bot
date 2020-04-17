from web.server import app
from src import bot

app = app.flask

if __name__ == '__main__':
	app.run()