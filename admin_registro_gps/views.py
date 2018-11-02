# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from admin_registro_gps.models import Monitor2, Monitor
#Create your views here.

def index(request):
	#limite=datetime.now().replace(day=2).strftime('%Y-%m-%d')
	#mon = Monitor(linha='688',data_inicio= datetime.now().strftime('%Y-%m-%d'), data_limite= limite)
    mon2 = Monitor2(linha = "688")
    #mon2.save()
    return render(request, 'index.html', {"mon" :mon2} )

