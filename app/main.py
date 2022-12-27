from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from app.models import mongdb
from app.models.book import BookModel



BASE_DIR = Path(__file__).resolve().parent


app = FastAPI()

templates = Jinja2Templates(directory=BASE_DIR/"templates")

@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    
    book = BookModel(keyword="파이썬", publisher="aa", price=123, image="adsf")
    print(await mongdb.engine.save(book))
    
    return templates.TemplateResponse("./index.html", {"request":request, "title":"콜렉터 북북이"})

@app.get("/search", response_class=HTMLResponse)
async def search(request:Request, q:str):
    return templates.TemplateResponse("./index.html", {"request":request, "title":"콜렉터 북북이", "keyword":q})


#app.on_event("startup") : 앱이 실행될때 실행되는 이벤트
@app.on_event("startup")
async def on_app_start():
    """ after app start """
    mongdb.connect()

#app.on_event("shutdown") : 서버가 shutdown이 됐을때 실행되는 이벤트
@app.on_event("shutdown")
async def on_app_shutdown():
    """ after app shut down """
    mongdb.close()