import requests
import base64
from django.http import HttpResponse

def auth(function):
    def middleware(request, *args, **kwargs):
        # Check if the 'Authorization' header exists
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header or not auth_header.startswith('Basic '):
            # return httpResponse as we are in the middleware
            return HttpResponse('Authorization header missing or invalid', status=401)
        
        # Extract and decode the credentials
        try:
            encoded_credentials = auth_header.split('Basic ')[1]
            decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8').split(':')
            username = decoded_credentials[0]
            password = decoded_credentials[1]
            # print(username)
            # print(password)
        except Exception as e:
            return HttpResponse('Invalid authorization format', status=401)

        # URL for the interservice call
        url = 'http://127.0.0.1:8000/api/dummy/'

        # Make the interservice request
        try:
            res = requests.get(url, auth=(username, password))
        except Exception as e:
            return HttpResponse('Interservice request failed', status=500)

        if res.status_code != 200:
            return HttpResponse('Invalid username or password', status=401)

        # Call the wrapped function
        return function(request, *args, **kwargs)

    return middleware
