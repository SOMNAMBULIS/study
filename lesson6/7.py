"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

from pyowm import OWM


owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()
city = input('Enter city: ').capitalize() or 'Minsk'
obs = mgr.weather_at_place(city)
w = obs.to_dict()
print(f'City: {w['location']['name']} | Weather: {w['weather']['detailed_status']} | Temperature: {obs.weather.temperature('celsius')['temp']}')
