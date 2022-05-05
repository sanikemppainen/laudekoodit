from db import db


def add_post(lat, long, image, creator, teksti):
    sql = "INSERT INTO posts (lat, long, image, creator, teksti, created_at) VALUES (:lat, :long, :image, :creator, :teksti, NOW())"
    db.session.execute(
        sql,
        {
            "lat": lat,
            "long": long,
            "image": image,
            "creator": creator,
            "teksti": teksti,
        },
    )
    db.session.commit()


def get_posts():
    sql = "SELECT p.id, p.created_at, p.lat, p.long, p.teksti, i.name, i.data, u.id, u.name FROM posts p, images i, users u where p.image=i.id and p.creator=u.id ORDER BY p.created_at DESC"
    result = db.session.execute(sql)
    all_posts = result.fetchall()
    return all_posts
