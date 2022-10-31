from django.shortcuts import render
from django.http import HttpResponse
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from django.http import HttpRequest

def home( request: 'HttpRequest') -> HttpResponse:
    """Home Page"""
    return render(request, 'home.html')
