import requests
import json

OpenWeatherMap_api = '030b9098987b9ee49faeaef6fe11f4d8'

url = 'http://api.openweathermap.org/data/2.5/weather?id=184742&appid=030b9098987b9ee49faeaef6fe11f4d8'
json_obj = requests.get(url)
 
data = json.loads(json_obj.text)

print(data['main'])
print(data['coord']) 
print(data['name'])
print (data['weather'])



    
    

       
        

        
        
