from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from services.const import PHONES, ADMIN_MODEL_URL
from services.sms import SMS


class SendSMSView(LoginRequiredMixin, View):

    @staticmethod
    def post(request, *args, **kwargs):
        phones = request.session[PHONES]
        admin_model_url = request.session[ADMIN_MODEL_URL]
        if 'send_button' in request.POST:
            message = request.POST['message']
            if message:
                sms = SMS()
                sms.send_sms(message, phones)
                if len(phones) > 1:
                    messages.success(request, 'Сообщения отправлены.')
                else:
                    messages.success(request, 'Сообщение отправлено.')
            else:
                messages.warning(request, 'Текст сообщения пустой.')
        return redirect(admin_model_url)
