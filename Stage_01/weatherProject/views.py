from django.http import JsonResponse
import requests
# import ipinfo



def userip(request):
    name = request.GET['visitor_name']

    name = name.replace('"', '')

    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip is not None:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    payload = {'ip': ip, 'format': 'json'}
    api_result =  requests.get("https://geolocation-db.com/json/{}&position=true".format(ip))
    city = api_result.json()
    print(ip)
    cityName = city['city']

    weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid=3b6cb4536a3f0c99e3d357906ad951f9&units=metric'.format(cityName))
    temps = weather.json()
   
    # print(request.ipinfo.city)

    Temps = temps['main']['temp']

    data = {
        "client_ip": ip,
        "location": cityName,
        "greeting": f"Hello, {name}!, the temperature is {Temps} degrees Celcius in {cityName}"
    }
    

    return JsonResponse(data)