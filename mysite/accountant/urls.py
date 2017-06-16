from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'show_customer_statement/$', views.show_customer_statement, name='show_customer_statement'),
    url(r'customer_statement/$', views.customer_statement, name='customer_statement'),
    url(r'burdensheet/send_file/$', views.send_file, name='sned_file'),
]