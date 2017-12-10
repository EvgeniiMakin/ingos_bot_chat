from config import mapsAPIKeyGOOGLE
import requests
from math import sin, cos, sqrt, atan2, radians
def distance_map(ob_1_x,ob_1_y,ob_2_x,ob_2_y):
    R = 6373.0
    lat1 = radians(ob_1_x)
    lon1 = radians(ob_1_y)
    lat2 = radians(ob_2_x)
    lon2 = radians(ob_2_y)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance
def getDictMapsLoc(message, info):
    lat = message.location.latitude
    lon = message.location.longitude
    url = ""
    if (info =="Все клиники"):
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%f,%f&radius=10000&types=healt&keyword=hospital&language=ru&key=%s' % (lat, lon, mapsAPIKeyGOOGLE)
    elif (info == 'Клиники Будь Здоров'):
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%f,%f&radius=12000&types=health&name=Клиника Будь Здоров&language=ru&keyword=Ингосстрах&key=%s' % (lat, lon, mapsAPIKeyGOOGLE)
    elif (info ==  "Офисы"):
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=%f,%f&radius=10000&keyword=Ингосстрах&language=ru&key=%s' % (lat, lon, mapsAPIKeyGOOGLE)
    var = requests.get(url)
    var = var.json()
    return var

def MAPS(message, i, info):
    lat = message.location.latitude
    lon = message.location.longitude
    responseDict = getDictMapsLoc(message, info)
    object = responseDict["results"][i]
    dist = round(distance_map(lat, lon, object["geometry"]["location"]["lat"], object["geometry"]["location"]["lng"]), 1)
    name = object["name"]
    try:
        opening = object["opening_hours"]["open_now"]
    except KeyError:
        open = "Нет данных"
        opening = None

    if (opening == True):
        open = "Открыто"
    elif (opening == False):
        open = "Закрыто"

    try:
        rating = object["rating"]
    except KeyError:
        rating = "Нет данных"
    vicinity = object["vicinity"]
    return name, vicinity, open, rating, dist
