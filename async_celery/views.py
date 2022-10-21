from django.http import HttpResponse
from django.views import View
# from django.conf import settings
# from django.core.mail import send_mail
import datetime
import pytz
import json
from .tasks import send_async_email

utc_timezone = pytz.timezone('Asia/Calcutta')
class MyView(View):
    def get(self, request):
        resp = {}
        a = datetime.datetime.now(utc_timezone).strftime("%d-%m-%Y %H:%M:%S")
        resp['current_time'] = a
        send_async_email.delay()
        return HttpResponse(json.dumps(resp), content_type="application/json")