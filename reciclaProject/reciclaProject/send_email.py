from django.conf import settings
from django import template
from django.shortcuts import render
from django.template.loader import get_template
from templates import *
from django.core.mail import EmailMultiAlternatives

def send_email(data,type):
    if(type == 1):
        context = {'name':data["name"]}
        template = get_template('Correo_registro_proveedor.html')
        content = template.render(context)
        email = EmailMultiAlternatives(
            'Bienvenid@ a',
            'Recicla+ Bogotá - Proveedor',
            settings.EMAIL_HOST_USER,
            [data["email"]]
        )
        email.attach_alternative(content,'text/html')
        email.send()
    else: 
        if(type == 2):
            context = {'name':data["name"]}
            template = get_template('Correo_registro_reciclador.html')
            content = template.render(context)
            email = EmailMultiAlternatives(
                'Bienvenid@ a',
                'Recicla+ Bogotá - Reciclador',
                settings.EMAIL_HOST_USER,
                [data["email"]]
            )
            email.attach_alternative(content,'text/html')
            email.send()