from django.conf.urls import patterns, include, url
from django.contrib import admin
from myApp import views

admin.autodiscover()

urlpatterns = patterns('',
                       
    #the URL formatting works - the general URL returns all available data for that, the specialized you select a specific 
    #column, year, month and day
    url(r'^home/$', views.home),
    url(r'^sectors/$', views.sectors),
    #get a specific day for a field
    url(r'^sectors/([a-zA-Z_-]+)*/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.sectors),
    #range for specific field
    url(r'^sectors/([a-zA-Z_-]+)*/([0-9]{4})/([0-9]{2})/([0-9]{2})/to/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.sectors),
    
    url(r'^industry/$', views.industry),
    url(r'^industry/([a-zA-Z_-]+)*/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.industry),
    url(r'^industry/([a-zA-Z_-]+)*/([0-9]{4})/([0-9]{2})/([0-9]{2})/to/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.industry),
                       
    url(r'^companies/$', views.companies),
    url(r'^companies/([a-zA-Z_-]+)*/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.companies),
    url(r'^companies/([a-zA-Z_-]+)*/([0-9]{4})/([0-9]{2})/([0-9]{2})/to/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.companies),
                       
    url(r'^quotes/$', views.quotes),
    url(r'^quotes/([a-zA-Z_-]+)*/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.quotes),
    url(r'^quotes/([a-zA-Z_-]+)*/([0-9]{4})/([0-9]{2})/([0-9]{2})/to/([0-9]{4})/([0-9]{2})/([0-9]{2})/$', views.quotes),
                       
    url(r'^company/$', views.company),
   
    url(r'^sectors/([0-9]{1})/$', views.sectorHistory),    
    url(r'^industries/([0-9]+)*/$', views.industriesHistory),    

)
