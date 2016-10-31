#-*- coding: utf-8 -*-

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect

from .forms import SubscriptionForm


def landingpage(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            form_name = form.cleaned_data.get("name")
            form_email = form.cleaned_data.get("email")
            subject = "%s님의 구독확인 메일입니다."% (form_name)
            message = "파인드 에프피 메일 구독."
            from_email = settings.EMAIL_HOST_USER
            to_emails = [form_email, 'bychoi@fintalk.co.kr']

            # for val in to_emails:
            #     send_mail(subject, message, from_email, [val], fail_silently=False)
            context = {
                "flag": True,
                "name": form_name,
            }
            return render(request, 'landingpage/index.html/', context)
    else:
        form = SubscriptionForm()

    context = {
        "form": form,
        "flag": False,
    }

    return render(request, 'landingpage/index.html', context)
