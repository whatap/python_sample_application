from whatap import method_profiling
import requests
import time
@method_profiling
def test_method_profiling():
    requests.get(url="http://www.naver.com")
    requests.get(url="http://www.naver.com")
    requests.get(url="http://www.naver.com")
    time.sleep(60)
    return None