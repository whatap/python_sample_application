from loguru import logger
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException
from starlette.responses import HTMLResponse
import uvicorn
import requests

logger.add('whatap_sink.log', level='DEBUG', format="<level>{level: <8}</level> <green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>  -- {{ \"@txid\" : \"{txid}\" }} -- <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>")

app = FastAPI()

@app.get("/health_check")
async def example():
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

if __name__ == "__main__":
    uvicorn.run(app="server:app", host="0.0.0.0", port=9000, reload=True)