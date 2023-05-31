import os
from django.http import HttpResponse
import requests

# Create your views here.
# host = os.environ.get("HOST")

def app_main(request):
    print("app_main")
    return HttpResponse("home")

def get_client_ip(request):
    x_forwarded_for = request.META.get('X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def url1(request):
    x_forwarded_for = get_client_ip(request)
    ##환경 변수 없는 경우 host
    # if not host:
    #     return

    ##recursive 한 요청이 들어올 경우 return 해준다.
    data = request.GET.get('data', '')
    if data == "whatap_request":
        return

    requests.get(url="https://google.com")

    return HttpResponse(f"bmt/url1:{x_forwarded_for}")

def url2(request):
    requests.get(url="https://www.naver.com")
    return HttpResponse(f"bmt/url2")



