#bc3e62293cb831488ebd6acffa6ccddb
from pyowm import OWM
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here
owm = OWM('bc3e62293cb831488ebd6acffa6ccddb')  # You MUST provide a valid API key

place = input("Введи Город/страну: ")
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]
wind=w.wind()


print("В городе " + place + " Сейчас " + str(w.detailed_status))
print("Температура: " + str(temp))
print("Скорость ветра сейчас"+str(wind))


if temp<10:
    print("Мамочка, сейчас очень холодно, оденься нормально")
elif temp<20:
    print("Можешь не надевать шубу , на улице чуть чуть прохладно")
else:
    print("На улице Ташкент")
    import telebot
    input()



