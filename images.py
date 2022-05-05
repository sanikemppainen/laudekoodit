from db import db
from base64 import b64encode
from zlib import compress, decompress
from utils import decode_image


def check_tags():
    pass


def add_image(name, data):
    sql = "INSERT INTO images (name, data) VALUES (:name, :data)"
    image = db.session.execute(sql, {"name": name, "data": data})
    db.session.commit()
    return image


def get_images():
    result = db.session.execute("SELECT name, data FROM images")
    data = result.fetchall()
    if not data:
        return []
    data = data[0]
    return decode_image(data["data"])


def get_image_id(name):
    result = db.session.execute(
        "SELECT id FROM images WHERE name=:name", {"name": name}
    )
    id = result.fetchone()[0]
    return id
