from django.views.generic.edit import CreateView
from django.shortcuts import reverse
from .models import Alert
from .forms import AlertModelForm
from recipient.models import Recipient
from django.conf import settings
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message


class AlertCreateView(CreateView):
    model = Alert
    template_name = 'form.html'
    form_class = AlertModelForm

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            msg = email.message.Message()
            msg['Subject'] = f"[LGAlert] {self.object.title}"
            msg['From'] = settings.EMAIL_HOST_USER
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(self.object.content)
            s = smtplib.SMTP(host=settings.EMAIL_HOST, port=settings.EMAIL_PORT)
            s.starttls()
            s.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            for rec in Recipient.objects.filter(active=True):
                msg['To'] = rec.email
                s.sendmail(msg['From'], [msg['To']], msg.as_string())
            s.quit()
        return super(AlertCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('confirm')
