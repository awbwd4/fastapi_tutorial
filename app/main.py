from typing import Optional
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)


app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR/"templates")

@app.get("/", response_class=HTMLResponse)
async def root(request:Request):
    # print(request["headers"])
    return templates.TemplateResponse("./index.html", {"request":request, "title":"콜렉터 북북이"})


@app.get("/search", response_class=HTMLResponse)
async def search(request:Request, q:str):
    print(q)
    # print(request["headers"])
    return templates.TemplateResponse("./index.html", {"request":request, "title":"콜렉터 북북이", "keyword":q})




# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_time(request:Request, id:str,  data:Optional[str]=None):
#     # print(request["headers"])
#     return templates.TemplateResponse("./item.html", {"request":request, "id":id, "data":data})


