from web.server import app
from config import token
from vk_api.utils import get_random_id
import vk_api

api = vk_api.VkApi(token=token).get_api()

@app.on("message_new")
def h(event):
	user_id = event['object']['user_id']
	api.messages.send(
		message='Hello World!',
		random_id=get_random_id(),
		peer_id=user_id
	)