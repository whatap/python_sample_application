from loguru import logger
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends, Request
from starlette.responses import HTMLResponse
from starlette.middleware.errors import ServerErrorMiddleware
from fastapi.exception_handlers import http_exception_handler
import uvicorn
import requests

app = FastAPI()

app.add_middleware(middleware_class=ServerErrorMiddleware, handler=http_exception_handler)

@app.get("/health_check")
async def health_check():
    logger.info("whatap_loguru_1.3.4:/health_check")
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    requests.get(url="https://www.naver.com")
    raise HTTPException(status_code=400)

@app.get("/example", response_class=HTMLResponse)
async def example():
    logger.info("whatap_loguru_1.3.4:/example")
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    res = requests.get(url="https://www.naver.com")
    return HTMLResponse(status_code=res.status_code)

async def log_test(request:Request):
    logger.info(f"dependency")
    return request.url

@app.get("/sync_example", response_class=HTMLResponse)
def sync_example(test: str = Depends(log_test)):
    logger.info(f"whatap_loguru_1.3.4:/sync_example {test}")
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    res = requests.get(url="https://www.naver.com")
    return HTMLResponse(status_code=res.status_code)

@app.get("/memory", response_class=HTMLResponse)
def sync_memory(test: str = Depends(log_test)):
    logger.info(f"whatap_loguru_1.3.4:/sync_example {test}")
    test_list = []

    for i in range(0, 10000000):
        test_list.append(i)
    return HTMLResponse(status_code=200)

@app.get("/use_memory")
def use_memory():
    test_list = []
    for i in range(0, 10000000):
        test_list.append(i)
    return HTMLResponse(status_code=200)

@app.get("/async_exception_example", response_class=HTMLResponse)
async def async_exception_example(test: str = Depends(log_test)):
    logger.info(f"whatap_loguru_1.3.4:/async_exception_example {test}")
    start_time = datetime.now()
    while True:
        if datetime.now() - start_time > timedelta(seconds=1):
            break
    requests.get(url="https://www.naver.com")
    raise HTTPException(status_code=400)


if __name__ == "__main__":
    uvicorn.run(app="server:app", host="0.0.0.0", port=9000, reload=True)