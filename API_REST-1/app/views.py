from django.shortcuts import render
from app.models import Person


def home(request):
    persons = Person.objects.all()

    content = {
        'messages': persons
    }
    return render(request, 'home.html', content)
