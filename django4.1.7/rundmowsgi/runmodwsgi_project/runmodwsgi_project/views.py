import os

from django.http import HttpResponse
from django.shortcuts import render
import requests
import time

# Create your views here.
# host = os.environ["HOST"]

def main(request):
    return HttpResponse(f"main")

def inner_call_test_url_1(request):
    return HttpResponse(f"inner_call_test_url_1")

def inner_call_test_url_2(request):
    return HttpResponse(f"inner_call_test_url_2")

def inner_call_test_url_3(request):
    return HttpResponse(f"inner_call_test_url_3")

def inner_call_test_url_4(request):
    return HttpResponse(f"inner_call_test_url_4")
