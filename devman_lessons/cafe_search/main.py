import json
import os

import folium
import requests

from dotenv import load_dotenv
from flask import Flask
from geopy import distance

MARKERS_AMOUNT = 5


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()\
        ['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def make_map(my_latitude, my_longitude, new_structure):
    city_map = folium.Map(location=[my_latitude, my_longitude])
    folium.Marker(
        [my_latitude, my_longitude],
        popup=f"<i>Ваше местоположение</i>",
        icon=folium.Icon(color="red")
    ).add_to(city_map)
    tooltip = "Click me!"

    for marker in range(MARKERS_AMOUNT):
        cafe_latitude = new_structure[marker]['latitude']
        cafe_longitude = new_structure[marker]['longitude']
        cafe_name = new_structure[marker]['title']
        folium.Marker(
            [cafe_latitude, cafe_longitude],
            popup=f"<i>{cafe_name}</i>",
            icon=folium.Icon(color="green")
        ).add_to(city_map)

    city_map.save("index.html")


def make_new_structure(coordinates):
    my_longitude, my_latitude = coordinates
    
    with open("coffee.json", "r", encoding="CP1251") as my_file:
        file_contents = json.loads(my_file.read())

    new_structure = []

    for content in file_contents:
        longitude, latitude = content['geoData']['coordinates']
        caffe_distance = str(distance.distance(
            (my_latitude, my_longitude), (latitude, longitude)).km)

        cafe_location = {
            'title': content['Name'],
            'distance': caffe_distance,
            'latitude': latitude,
            'longitude': longitude
        }
        new_structure += [cafe_location]

    new_structure = sorted(new_structure, key=get_distance)

    make_map(my_latitude, my_longitude, new_structure)


def get_distance(user):
    return user['distance']


def get_index():
    with open('index.html') as file:
        return file.read()


def main():
    location = input('Введите местоположение: ')
    load_dotenv()
    api_key = os.getenv('API_KEY')
    coordinates = fetch_coordinates(api_key, location)
    make_new_structure(coordinates)
    app = Flask(__name__)
    app.add_url_rule('/', 'caffe_map', get_index)
    app.run('0.0.0.0')


if __name__ == "__main__":
    main()
