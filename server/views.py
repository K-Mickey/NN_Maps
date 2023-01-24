from django.shortcuts import render
from .utils import create_map


def index(request):
    create_map()
    return render(request, 'nn_map.html')
