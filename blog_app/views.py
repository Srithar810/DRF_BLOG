from django.shortcuts import render
from django.http import JsonResponse

def blog_list(request):
    data = {
        'message': 'Hello World'
    }
    return JsonResponse(data)
