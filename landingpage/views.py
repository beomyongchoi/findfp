#-*- coding: utf-8 -*-

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .forms import SubscriptionForm
from .models import Subscription

import json


def landingpage(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     response_data = {}
    #
    #     subscription = Subscription(name=name, email=email)
    #     subscription.save()
    #
    #     response_data['result'] = 'Create post successful!'
    #     response_data['subscription_pk'] = subscription.pk
    #     response_data['name'] = subscription.name
    #     response_data['email'] = subscription.email
    #
    #     return HttpResponse(
    #         json.dumps(response_data),
    #         content_type="application/json"
    #     )
    #
    # else:
    #     form = SubscriptionForm()

    form = SubscriptionForm()

    context = {
        "form": form,
    }

    return render(request, 'landingpage/index.html', context)


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        response_data = {}

        subscription = Subscription(name=name, email=email)

        response_data['subscription_pk'] = subscription.pk
        response_data['name'] = subscription.name
        response_data['email'] = subscription.email

        if Subscription.objects.filter(email=email).exists():
            response_data['email'] = 'email_existed'

        else:
            subscription.save()

            subject = "%s님의 구독확인 메일입니다."% (subscription.name)
            message = "파인드 에프피 메일 구독 테스트."

            from_email = settings.EMAIL_HOST_USER
            to_emails = ['bychoi@fintalk.co.kr', ]
            # to_emails = [email, 'bychoi@fintalk.co.kr',]

            for val in to_emails:
                send_mail(subject, message, from_email, [val], fail_silently=False)

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
