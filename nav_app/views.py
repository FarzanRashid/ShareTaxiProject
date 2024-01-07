from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import RideRequest


@csrf_exempt
def book_taxi(request):
    if request.method == 'POST':
        try:
            json_data = request.body.decode('utf-8')
            data = json.loads(json_data)
            model_riderequest = RideRequest(dropoff_location=data['dropoff_location'],
                                            departure_time=data['departure_time'],
                                            email=data['email'],
                                            pickup_location=data['pickup_location'],
                                            date=data['date']
                                            )
            model_riderequest.save()
            response_data = {'success': True}
            return JsonResponse(response_data, status=200)
        except ValueError as e:
            response_data = {'success': False, 'error': "Invalid data"}
            return JsonResponse(response_data)
        except Exception as e:
            response_data = {'success': False, 'error': "Invalid data"}
            return JsonResponse(response_data, status=400)
    else:
        response_data = {'error': 'Invalid request method'}
        return JsonResponse(response_data, status=400)
