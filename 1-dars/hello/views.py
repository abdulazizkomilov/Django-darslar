from django.http import HttpResponse
from django.views.generic import TemplateView
import datetime

def hello(response):
    salom = '<h1>hello world</h1>'
    return HttpResponse(salom)

def sana_vaqt(response):
    hozir = datetime.datetime.now()
    time = f'<h1>Bugungi sana va vaqt - {hozir.strftime("%d-%m-%Y, %H:%M")}</h1>'
    return HttpResponse(time)

class Welcome(TemplateView):
    template_name = 'index.html'

