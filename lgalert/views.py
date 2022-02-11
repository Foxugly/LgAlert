from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from alert.forms import AlertModelForm


def home(request):
    template = loader.get_template('index.html')
    context = {'title': "[LGAlert] Home"}
    return HttpResponse(template.render(context, request))


def get_form(request):
    if request.method == 'POST':
        form = AlertModelForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return HttpResponseRedirect('/confirm/')
    else:
        form = AlertModelForm()
    template = loader.get_template('form.html')
    context = {'form': form, 'title': "[LGAlert] Form"}
    return HttpResponse(template.render(context, request))

def get_confirm(request):
    template = loader.get_template('confirm.html')
    context = {'title': "[LGAlert] Confirm"}
    return HttpResponse(template.render(context, request))
