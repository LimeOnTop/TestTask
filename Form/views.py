from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from Form.forms import MessageForm


def message(request):
    keys = {'form': MessageForm(),
            'title': 'Friendly Message',
            'attrs': '?name=Rekruto&message=Давай дружить!'
            }
    return render(request, 'Form/message_form.html', keys)


def result(request):
    name = request.GET.get('name', '')
    text = request.GET.get('message', '')
    return render(request, 'Form/message_result.html', {'name': name, 'text': text})


def standard(request: HttpRequest):
    name = request.GET.get('name', '')
    text = request.GET.get('message', '')
    return render(request, 'Form/message_standard.html', {'name': name, 'text': text})
# Create your views here.
