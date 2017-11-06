#!/usr/bin/python
# -*- coding: utf-8 -*-

import WeatherForcast

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def printList(category, value):
	print(bcolors.OKBLUE + bcolors.BOLD + category + ": " + bcolors.ENDC + value)

def printHead(value):
	print(bcolors.OKGREEN + bcolors.BOLD + "-----" + value + "-----" + bcolors.ENDC)

# Get the weather forcast
burien_code = "5788516"
eburg_code = "5793639"

#print(WeatherForcast.getWeatherReport(burien_code))
#print(WeatherForcast.getWeatherReport(eburg_code))

printHead("Weather Report")
printList("Burien", "\n" + WeatherForcast.getWeatherReport(5788516))
printList("Ellensburg", "\n" + WeatherForcast.getWeatherReport(5793639))