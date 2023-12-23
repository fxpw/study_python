import os
from flask import Flask, render_template, request
from functools import wraps
import asyncio


# def async_action(f):
# 	@wraps(f)
# 	def wrapped(*args, **kwargs):
# 		return asyncio.run(f(*args, **kwargs))

# 	return wrapped


# Создаем экземпляр Flask, указывая папку с шаблонами
flask_web_app = Flask(
	import_name="web-app",
	template_folder=os.path.abspath("./lesson16/templates"),
	static_folder=os.path.abspath("./lesson16/static"),
)


@flask_web_app.route("/")
async def index(seatch_text: str = ""):
	return render_template(
		"index.html",
	)


@flask_web_app.route("/", methods=["POST"])
async def course_search_get():
	# Как получть данные формы
	text = request.form["input_text"]
	return await index(text)


async def StartWebApp():
	flask_web_app.run(debug=True)
