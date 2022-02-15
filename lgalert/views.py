from django.http import HttpResponse
from django.template import loader


def home(request):
    template = loader.get_template('index.html')
    context = {'title': "[LGAlert] Home"}
    return HttpResponse(template.render(context, request))


def confirm(request):
    template = loader.get_template('confirm.html')
    context = {'title': "[LGAlert] Confirm"}
    return HttpResponse(template.render(context, request))
