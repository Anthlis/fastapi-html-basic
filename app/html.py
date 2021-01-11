from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

from app.model import spell_number

app = FastAPI()
templates = Jinja2Templates(directory='templates/')


def save_to_text(content, filename):
    filepath = 'data/{}.txt'.format(filename)
    with open(filepath, 'w') as f:
        f.write(content)
    return filepath


@app.get('/')
def read_form():
    return 'hello world'


@app.get('/form')
def form_post(request: Request):
    result = 'Type a number'
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@app.post('/form')
def form_post(request: Request, num: int = Form(...)):
    result = spell_number(num)
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result, 'num': num})