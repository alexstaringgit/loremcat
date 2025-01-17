import os
import random

from flask import Flask
from flask import send_from_directory

from config import IMAGES_PATH
import flickr


app = Flask(__name__)


@app.route("/")
def homepage():
    path = IMAGES_PATH / "landscape"
    files = list(path.glob("*.jpg"))
    file = random.choice(files)
    return send_from_directory(path, file.name)


@app.route("/portrait")
def portrait():
    path = IMAGES_PATH / "portrait"
    files = list(path.glob("*.jpg"))
    file = random.choice(files)
    return send_from_directory(path, file.name)


@app.route("/download-images")
def download_images():
    if os.getenv("ENABLE_DOWNLOAD_ROUTE") != "1":
        return "nope"
    flickr.fetch()
    return ""


@app.route("/stats")
def stats():
    output = ""

    output += f"<p>images path: {IMAGES_PATH}</p>"

    nb_landscape = len(
        list((IMAGES_PATH / "landscape").glob("*.jpg")),
    )
    output += f"<p>nb. landscape: {nb_landscape}</p>"

    nb_portrait = len(
        list((IMAGES_PATH / "portrait").glob("*.jpg")),
    )
    output += f"<p>nb. portrait: {nb_portrait}</p>"

    return output


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
