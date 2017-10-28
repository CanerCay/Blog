# -*- coding: utf-8 -*-
'''
Created on Mar 20, 2011

@author: Mourad Mourafiq

@license: closed application, My_licence, http://www.binpress.com/license/view/l/6f5700aefd2f24dd0a21d509ebd8cdf8

@copyright: Copyright © 2011

other contributers:
'''
from django.shortcuts import render_to_response,render
from django.template import RequestContext


def home(request, template_name="index.html"):
    return render(request,template_name)