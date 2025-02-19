from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/projetos", response_class=HTMLResponse)
def projetos(request: Request):
    return templates.TemplateResponse("projetos.html", {"request": request})

@app.get('/contatos', response_class=HTMLResponse)
def sobre(request:Request):
    return templates.TemplateResponse('contato.html', {"request":request})

@app.get('/certificados', response_class=HTMLResponse)
def certificados(request:Request):
    return templates.TemplateResponse('certificados.html', {'request':request})

#página projetos
@app.get('/web-scraping-sp', response_class=HTMLResponse)
def pag_webscrapingsp(request:Request):
    return templates.TemplateResponse('pag_webscrapingsp.html', {'request':request})
@app.get('/meu-portfolio', response_class=HTMLResponse)
def pag_webscrapingsp(request:Request):
    return templates.TemplateResponse('pag_meuportfolio.html', {'request':request})
@app.get('/news-bot', response_class=HTMLResponse)
def pag_webscrapingsp(request:Request):
    return templates.TemplateResponse('pag_newsbot.html', {'request':request})