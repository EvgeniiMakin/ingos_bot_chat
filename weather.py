# -*- coding: utf-8 -*-

from config import weatherApiKey
import urllib.request
import json
import datetime


def getDictByCityNow(city):
    city = city.replace(" ", "%20")
    var = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=%s&units=metric' % (city, weatherApiKey))
    var = var.read().decode("utf-8")
    var = json.loads(var)
    return var


def getDictByGeoNow(message):
    lat = message.location.latitude
    lon = message.location.longitude
    var = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?lat=%f&lon=%f&APPID=%s&units=metric' % (lat, lon, weatherApiKey))
    var = var.read().decode("utf-8")
    var = json.loads(var)
    return var


def getDictByCityForecast(city):
    city = city.replace(" ", "%20")
    var = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s&units=metric&cnt=13' % (city, weatherApiKey))
    var = var.read().decode("utf-8")
    var = json.loads(var)
    return var


def getDictByGeoForecast(message):
    lat = round(message.location.latitude)
    lon = round(message.location.longitude)
    var = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?lat=%f&lon=%f&APPID=%s&units=metric&cnt=13' % (lat, lon, weatherApiKey))
    var = var.read().decode("utf-8")
    var = json.loads(var)
    return var


def getWeather(responseDict):
    weather = responseDict["weather"]
    weather = weather[0]
    main = weather["main"]
    description = weather["description"]
    wind = responseDict["wind"]["speed"]
    if main.lower() == description.lower():
        description = ""
    else:
        description = ", " + weather["description"]
    return main, description, wind


def getTemp(responseDict):
    globalTemp = responseDict["main"]
    celsius = globalTemp["temp"]
    humidity = globalTemp["humidity"]
    return celsius, humidity


def byCity(city):
    responseDict = getDictByCityNow(city)
    cityName = responseDict["name"]
    country = responseDict["sys"]
    country = country["country"]
    main, description, wind = getWeather(responseDict)
    celsius, humidity = getTemp(responseDict)
    return cityName, country, main, description, celsius, humidity, wind


def byGeo(message):
    responseDict = getDictByGeoNow(message)
    cityName = responseDict["name"]
    country = responseDict["sys"]
    country = country["country"]
    main, description, wind = getWeather(responseDict)
    celsius, humidity = getTemp(responseDict)
    return cityName, country, main, description, celsius, humidity, wind


def byCityLater(city):
    responseDict = getDictByCityForecast(city)
    city = responseDict["city"]
    cityName = city["name"]
    country = city["country"]
    responseDict = responseDict["list"][0]
    main, description, wind = getWeather(responseDict)
    celsius, humidity = getTemp(responseDict)
    return cityName, country, main, description, celsius, humidity, wind


def byGeoLater(message):
    responseDict = getDictByGeoForecast(message)
    city = responseDict["city"]
    cityName = city["name"]
    country = city["country"]
    responseDict = responseDict["list"][0]
    main, description, wind = getWeather(responseDict)
    celsius, humidity = getTemp(responseDict)
    return cityName, country, main, description, celsius, humidity, wind


def byGeoTomorow(message):
    responseDict = getDictByGeoForecast(message)
    city = responseDict["city"]
    cityName = city["name"]
    country = city["country"]
    responseDict = responseDict["list"]
    lst = []
    for i in range(len(responseDict)):
        x = responseDict[i]
        value = datetime.datetime.fromtimestamp(int(x["dt"]))
        v = value.strftime('%H')
        lst.append(v)
    index = [i for i, v in enumerate(lst) if v == '09']
    responseDict = responseDict[index[0]+1]
    main, description, wind = getWeather(responseDict)
    celsius, humidity = getTemp(responseDict)
    return cityName, country, main, description, celsius, humidity, wind

def byCityTomorow(city):
    responseDict = getDictByCityForecast(city)
    city = responseDict["city"]
    cityName = city["name"]
    country = city["country"]
    responseDict = responseDict["list"]
    lst = []
    for i in range(len(responseDict)):
        x = responseDict[i]
        value = datetime.datetime.fromtimestamp(int(x["dt"]))
        v = value.strftime('%H')
        lst.append(v)
    index = [i for i, v in enumerate(lst) if v == '09']
    responseDict = responseDict[index[0]+1]
    main, description, wind = getWeather(responseDict)
    celsius, humidity = getTemp(responseDict)
    return cityName, country, main, description, celsius, humidity, wind