import base64
from django.http import HttpResponse
from django.contrib.auth import authenticate

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

        user = authenticate(username=username, password=password)
        if not user: 
            return HttpResponse('something wrong with user and password', status=401)

        # Call the wrapped function
        return function(request, *args, **kwargs)

    return middleware
