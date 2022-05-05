import requests
from users import create_user

BASE_URL = "https://hackathlon.nitorio.us"


def get_user_data():
    user_data = requests.get(f"{BASE_URL}/users")
    location_data = requests.get(f"{BASE_URL}/coordinates")
    users = user_data.json()
    locations = location_data.json()

    data = {}
    for user in users:
        data[user["id"]] = {
            "name": user["name"],
            "email": user["email"],
            "profile_image_url": user["imageUrl"],
        }
    for location in locations:
        data[location["userId"]]["coordinates"] = location["coordinates"]

    return data


def get_current_user():
    # data = requests.get(f"{BASE_URL}/me")
    data = {
        "id": "U6",
        "name": "Mette Backman",
        "email": "mette.backman@nitor.com",
        "fromFlightId": "F3",
        "toFlightId": "F1",
        "imageUrl": "www.foo.jpg",
        "activityId": "A1",
        "coordinates": {"lat": 66.16769778169346, "long": 29.13931099097882},
    }
    return data


def insert_users():
    users = get_user_data()
    for id, data in users.values():
        name = data["name"]
        email = data["email"]
        profile_image_url = data["profile_image_url"]
        create_user(id, name, email, profile_image_url)


if __name__ == "__main__":
    # get_user_data()
    # get_current_user()
    insert_users()
