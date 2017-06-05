# -*- coding: utf-8 -*-
from .forms import BurdenSheetForm, ProductOrderForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import os, tempfile, zipfile
from wsgiref.util import FileWrapper

def index(request):
    return render(request, 'accountant/index.html')

def send_file(request):
    """                                                                         
    Send a file through Django without loading the whole file into              
    memory at once. The FileWrapper will turn the file object into an           
    iterator for chunks of 8KB.                                                 
    """
    filename = "/Users/curlylrt/Desktop/BUSD.xlsx" # Select your file here.                                
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='mimetype/submimetype')
    response['Content-Length'] = os.path.getsize(filename)
    response['Content-Disposition'] = 'attachment; filename=DownloadedEval.xlsx'
    return response