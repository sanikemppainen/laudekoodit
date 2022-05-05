from db import db


def get_users():
    sql = "SELECT id, name, email FROM users"
    users = sql.execute(sql)
    return users.fetchall()


def create_user(id, name, email, profile_image_url):
    sql = "INSERT INTO users (id, name, email, profile_image_url) VALUES (:id, :name, :email, :image_url"
    db.session.execute(
        sql, {"id": id, "name": name, "email": email, "image_url": profile_image_url}
    )
    db.session.commit()
