from django.forms import ModelForm
from captcha.fields import CaptchaField
from alert.models import Alert


class AlertModelForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Alert
        fields = ['title', 'content', 'captcha']
