#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import urllib2
import time

class Forecast:
	index = 0
	cityName = ""
	weatherTime = ""
	temperature = 0
	rainfall = 0
	snowfall = 0
	weatherGroup = ""
	weatherCondition = ""

def getUrl(id):
	return "http://api.openweathermap.org/data/2.5/forecast?id=" + str(id) + "&APPID=933f835cb1b6ada5fc2c27396d93d5b6"

def downloadPage(url):
	page = urllib2.urlopen(url)
	return page.read()

def readData(page):
	data = json.loads(page)

	length = 5
	f = [Forecast() for i in range(length)]
	for i in range(length):
		index = i + i * 3
		f[i].index = index
		f[i].cityName = str(data["city"]["name"])
		f[i].temperature = int((float(data["list"][index]["main"]["temp"]) * 9 / 5) - 459.67)
		f[i].weatherGroup = str(data["list"][index]["weather"][0]["main"])
		f[i].weatherCondition = str(data["list"][index]["weather"][0]["description"])
		f[i].weatherTime = time.strftime('%a, %d %b %I %p', time.localtime(data["list"][index]["dt"]))
		if("rain" in data["list"][index] and data["list"][index]["rain"] > 0):
			if("3h" in data["list"][index]["rain"]):
				f[i].rainfall = int(data["list"][index]["rain"]["3h"] * 100)
		if("snow" in data["list"][index] and data["list"][index]["snow"] > 0):
			if("3h" in data["list"][index]["snow"]):
				f[i].snowfall = int(data["list"][index]["snow"]["3h"] * 100)
	return f

def formatData(fore):
	if fore is None:
		return ""
	weatherString = ""
	for i in range(len(fore)):
		weatherString += fore[i].weatherTime
		weatherString += " -- " + str(fore[i].temperature) + "°"
		if(fore[i].rainfall > 0):
			weatherString += " -- " + str(fore[i].rainfall) + "mm rain"
		if(fore[i].snowfall > 0):
			weatherString += " -- " + str(fore[i].rainfall) + "mm snow"
		weatherString += " -- " + fore[i].weatherGroup
		weatherString += " -- " + fore[i].weatherCondition
		if(i < len(fore) - 1):
			weatherString += "\n"
	return weatherString


def getFormattedData(cityId):
	url = getUrl(cityId)
	page = downloadPage(url)
	data = readData(page)
	name = data[0].cityName
	formatted = formatData(data)

	return formatted
	output = open(name + "Report.txt", "w")
	output.write(formatted)
	output.close()

def writeToFile(filename, filedata):
	output = open(filename, "w")
	output.write(filedata)
	output.close()


def getWeatherReport(cityId):
	url = getUrl(cityId)
	page = downloadPage(url)
	data = readData(page)
	name = data[0].cityName
	formatted = formatData(data)

	return formatted
