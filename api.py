import requests
import json

OpenWeatherMap_api = '030b9098987b9ee49faeaef6fe11f4d8'

url = 'http://api.openweathermap.org/data/2.5/weather?id=184742&appid=030b9098987b9ee49faeaef6fe11f4d8'

api_key = OpenWeatherMap_api

city_id = input('Please Enter city id ')
final_url ='http://api.openweathermap.org/data/2.5/weather?id=' + city_id + '&appid=' + api_key
json_obj = requests.get(final_url)
data = json.loads(json_obj.text)


print(data['main'])
print(data['coord']) 
print(data['name'])
print (data['weather'])

# Examples of city ids
#'184742' for Nairobi
# 1273294 for Delhi
# 524901 for Moscow