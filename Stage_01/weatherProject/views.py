from django.http import JsonResponse
import requests



def userip(request):
    name = request.GET['visitor_name']
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip is not None:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    payload = {'ip': ip, 'format': 'json'}
    api_result = requests.get('https://api.ip2location.io/', params=payload)
    city = api_result.json()
    cityName = city['city_name']

    weather = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&appid=3b6cb4536a3f0c99e3d357906ad951f9&units=metric'.format(cityName))
    temps = weather.json()
   

    Temps = temps['main']['temp']

    data = {
        "client_ip": ip,
        "location": cityName,
        "greeting": f"Hello, {name}!, the temperature is {Temps} degrees celcius in {cityName}"
    }
    

    return JsonResponse(data)