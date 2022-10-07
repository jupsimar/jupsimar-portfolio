import urllib.request
import json

location = input("Where do you want the weather for? ")

url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=af7824ae8c177c05cefaccff7bc6c572'

response = urllib.request.urlopen(url)
result = json.loads(response.read())

print(round(result["main"]["temp"]-273.15,2),"C")
print(round((result["main"]["temp"]-273.15)*9/5+32,2),"F")

temp_c = round(result["main"]["temp"]-273.15,2)
temp_f = round((result["main"]["temp"]-273.15)*9/5+32,2)

if temp_c > 30:
    print("Wear tshirt and sunscreen, its hot!")
elif temp_c > 10:
    print("Wear a jacket")
elif temp_c < -10:
    print("Its very cold! Everything that's there in the wardrobe")        