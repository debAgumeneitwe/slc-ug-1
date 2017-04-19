import requests
import json

openweathermap_api = '030b9098987b9ee49faeaef6fe11f4d8'

url = 'http://api.openweathermap.org/data/2.5/weather?id=184742&appid=030b9098987b9ee49faeaef6fe11f4d8'
json_obj = requests.get(url)
 
data = json.load(json_obj.text)


for item in data:
    print (item['coord'])
    print (item['country'])
    print (item('id'))
    print (item['name'])
    

       
        

        
        
