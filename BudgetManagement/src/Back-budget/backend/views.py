# backend/views.py

from django.http import JsonResponse

def home(request):
    data = {'message': 'Welcome to the budget app!'}
    return JsonResponse(data)
