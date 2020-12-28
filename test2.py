import pyowm
from pyowm.utils import config
from pyowm.utils import timestamps

owm = pyowm.OWM('4443dc30d5e3d12cf9f44e04604037c6')
mgr = owm.weather_manager()

place = input("В якому місті/країні?: ")

observation = mgr.weather_at_place('place')
w = observation.weather
w.detailed_status 
temp = w.temperature('celsius')["temp"]
print( "В місті " + place + " зараз " + str(w.wind()) + str(w.rain))
print("Зараз близько " + str(temp))

if temp < 10:
	print ("зараз ппц холодно!")
elif temp > 15:
	print ("виходь в трусєлях?!")
