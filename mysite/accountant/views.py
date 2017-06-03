# -*- coding: utf-8 -*-
from .forms import BurdenSheetForm, ProductOrderForm
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class AddBurdenSheetView(CreateView):
    template_name = 'accountant/edit_burden_sheet.html'
    form_class = BurdenSheetForm

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super(ContactView, self).form_valid(form)


# def generateEditBurdenSheetView(request):
#         if request.method == 'POST': # If the form has been submitted...
#             burdensheet_form = BurdenSheetForm(request.POST, prefix = "burdensheet")
#             productorder_form = ProductOrderForm(request.POST, prefix = "b")
#             c_form = CForm(request.POST, prefix = "c")
#             if primary_form.is_valid() and b_form.is_valid() and c_form.is_valid(): # All validation rules pass
#                     print "all validation passed"
#                     primary = primary_form.save()
#                     b_form.cleaned_data["primary"] = primary
#                     b = b_form.save()
#                     c_form.cleaned_data["primary"] = primary
#                     c = c_form.save()
#                     return HttpResponseRedirect("/viewer/%s/" % (primary.name))
#             else:
#                     print "failed"

#         else:
#             primary_form = PrimaryForm(prefix = "primary")
#             b_form = BForm(prefix = "b")
#             c_form = Form(prefix = "c")
#      return render_to_response('multi_model.html', {
#      'primary_form': primary_form,
#      'b_form': b_form,