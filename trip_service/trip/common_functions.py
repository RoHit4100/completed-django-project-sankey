import requests
from django.http import JsonResponse


def interserviceCall(url, request_method, data=None):
    
    try:
        if request_method in ['POST', 'GET']:
            if request_method == 'GET':
                response = requests.get(url)
                
                # if response.status_code == 200:
                #     data = response.json()
                #     return JsonResponse({'data': data}, status=200)
                
            elif request_method == 'POST':
                
                print(data)    
                response = requests.post(url, json=data)
                print(response.status_code)
                # if res.status_code == 200
                #     return JsonResponse({'message': 'data is successfully added'}, status=201)      

            return JsonResponse({'data':response.json()}, status = response.status_code)
        else:
            return JsonResponse({'method': 'not allowed'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)