from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import GetUserInfo


@csrf_exempt
def book_taxi(request):
    if request.method == 'POST':
        try:
            json_data = request.body.decode('utf-8')
            data = json.loads(json_data)
            my_model = GetUserInfo(location=data['location'], departure_time=data['departure_time'],
                                   email=data['email'])
            my_model.save()
            response_data = {'success': True}
            return JsonResponse(response_data)
        except ValueError as e:
            response_data = {'success': False, 'error': str(e)}
            return JsonResponse(response_data)
    else:
        response_data = {'error': 'Invalid request method'}
        return JsonResponse(response_data, status=400)
