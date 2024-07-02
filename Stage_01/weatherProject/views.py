from django.shortcuts import HttpResponse

def userip(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip is not None:
        ip = user_ip.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return HttpResponse("Welcome user: {}".format(ip))