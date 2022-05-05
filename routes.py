import json
from flask import render_template, redirect, request, session
from app import app
from images import get_image_id, get_images, add_image
from posts import add_post, get_posts
from user_service import get_current_user
from utils import decode_image

current_user = get_current_user()


@app.route("/")
def index():
    return redirect("/feed")


@app.route("/feed", methods=["POST", "GET"])
def feed():
    if request.method == "POST":
        image = request.files["image"]
        post_text = request.form["text"]
        name = image.filename
        data = image.read()
        if name.__contains__(".jpg") or name.__contains__(".jpeg"):
            image = add_image(name, data)
            image_id = get_image_id(name)
            add_post(
                current_user["coordinates"]["lat"],
                current_user["coordinates"]["long"],
                image_id,
                current_user["id"],
                post_text,
            )
        return redirect("/feed")
    posts = get_posts()
    posts = [
        {
            "id": post[0],
            "created_at": post[1],
            "lat": post[2],
            "long": post[3],
            "teksti": post[4],
            "image_name": post[5],
            "image_data": decode_image(post[6]),
            "user_id": post[7],
            "user_name": post[8],
        }
        for post in posts
    ]
    
    json_posts = [json.dumps(post) for post in [{'lat': p['lat'], 'long': p['long']} for p in posts]]
    return render_template("feed.html", posts=posts, json_posts=json_posts)
