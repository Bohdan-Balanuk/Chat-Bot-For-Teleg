import requests #requests - запити до сервера за допомогою API

# https://api.open-meteo.com/v1/forecast - посилнна на API
# Error 404 = Not Found
# Error 400 = Bad Request
# Response 200 = правильна відповідь

def get_info_about_weather(location):
    wether_params = {
        'latitude': location[0],
        'longitude': location[1],
        'current_weather': True
    }

    # запитати і зберегти відповідь у змінну response
    response = requests.get('https://api.open-meteo.com/v1/forecast', params=wether_params)
    data = response.json() # зберігається json-відповідь

    tmperatura_citi = data['current_weather']['temperature']

    return tmperatura_citi

def get_locaion_citi(citi):
    location_perms = {
        'name': citi,
    }
    
    response = requests.get('https://geocoding-api.open-meteo.com/v1/search', params=location_perms)
    data = response.json()
    i = 0

    for i in range(len(data['results'])):
        print(data['results'][i]['latitude'])

    # location_citit = [
    #     data['results'][0]['latitude'],
    #     data['results'][0]['longitude']
    # ]

    # return location_citit


ask_citi = input("Введіть назву міста (АНГЛІЙСЬКОЮ МОВОЮ), температуру в якого ви хочете взанти? ")

location = get_locaion_citi(ask_citi)

#temperatura_citi = get_info_about_weather(location)

print("Місце знаходження міста: " + str(location))
#print("Температура в місті: " + str(temperatura_citi))
