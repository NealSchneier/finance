from django.shortcuts import render
from django.http import StreamingHttpResponse
from models import Sector, Industry, Quotes, Company, Companies, Sectors, Industries
from django.core import serializers
from django.template import Template
import datetime


# Create your views here.
def home(request):
  #execfile("./neuralNetwork/rnn.py")
  return render(request, 'base.html')

# def sectors(request):
#   data = serializers.serialize("json", Sector.objects.all())
#   return StreamingHttpResponse(data)

def sectors(request, atr=None, year=None, month=None, day=None, toYear=None, toMonth=None, toDay=None):  
  if toYear != None and toMonth !=None and toDay !=None:
    query = 'select * from sectors where date(curr_date) >= "%s-%s-%s" and date(curr_date) <= "%s-%s-%s" order by %s' % (str(year), str(month), str(day), str(toYear), str(toMonth), str(toDay), atr)
    sectors = Sectors.objects.raw(query)
  elif atr != None and year != None and month != None and day != None:
    query = 'select * from sectors where date(curr_date) = "%s-%s-%s" order by %s' % (str(year), str(month), str(day), atr)
    sectors = Sectors.objects.raw(query)
  else:
    sectors = Sectors.objects.all()
  
  sectors = serializers.serialize("json", sectors)
  return StreamingHttpResponse(sectors)


# def industry(request):
#   data = serializers.serialize("json", Industry.objects.all())
#   return StreamingHttpResponse(data)

def industry(request, atr=None, year=None, month=None, day=None, toYear=None, toMonth=None, toDay=None):  
  if toYear != None and toMonth !=None and toDay !=None:
    query = 'select * from industries where date(curr_date) >= "%s-%s-%s" and date(curr_date) <= "%s-%s-%s" order by %s' % (str(year), str(month), str(day), str(toYear), str(toMonth), str(toDay), atr)
    data = Industry.objects.raw(query)
  elif atr != None and year != None and month != None and day != None:
    query = 'select * from industries where date(curr_date) = "%s-%s-%s" order by %s' % (str(year), str(month), str(day), atr)  
    data = Industry.objects.raw(query)
  else:
    data = Industry.objects.all()
  data = serializers.serialize("json", data)
  return StreamingHttpResponse(data)

# def quotes(request):
#   data = serializers.serialize("json", Quotes.objects.all())
#   return StreamingHttpResponse(data)

def quotes(request, atr=None, year=None, month=None, day=None, toYear=None, toMonth=None, toDay=None):  
  if toYear != None and toMonth !=None and toDay !=None:
    query = 'select * from quotes where date(curr_date) >= "%s-%s-%s" and date(curr_date) <= "%s-%s-%s" order by %s' % (str(year), str(month), str(day), str(toYear), str(toMonth), str(toDay), atr)
    data = Quotes.objects.raw(query)
  elif atr != None and year != None and month != None and day != None:
    query = 'select * from quotes where date(curr_date) = "%s-%s-%s" order by %s' % (str(year), str(month), str(day), atr)
    data = Quotes.objects.raw(query)
  else:
    data = Quotes.objects.all()
  data = serializers.serialize("json", data)
  return StreamingHttpResponse(data)

def company(request):
  data = serializers.serialize("json", Company.objects.all())
  return StreamingHttpResponse(data)



# def companies(request):
#   data = serializers.serialize("json", Companies.objects.all())
#   return StreamingHttpResponse(data)

def companies(request, atr=None, year=None, month=None, day=None, toYear=None, toMonth=None, toDay=None):  
  if toYear != None and toMonth !=None and toDay !=None:
    query = 'select * from companies where date(curr_date) >= "%s-%s-%s" and date(curr_date) <= "%s-%s-%s" order by %s limit 10' % (str(year), str(month), str(day), str(toYear), str(toMonth), str(toDay), atr)
    data = Companies.objects.raw(query)
  elif atr != None and year != None and month != None and day != None:
    query = 'select * from companies where date(curr_date) = "%s-%s-%s" order by %s limit 10' % (str(year), str(month), str(day), atr)
    data = Companies.objects.raw(query)
  else:
    data = Companies.objects.all()[:10]
  data = serializers.serialize("json", data)
  return StreamingHttpResponse(data)

def sectorHistory(request, sectorId=None):
  data = Sectors.objects.filter(sector=sectorId)
  data = serializers.serialize("json", data)
  return StreamingHttpResponse(data)

def industriesHistory(request, industryId=None):
  data = Industries.objects.filter(industry=industryId)
  data = serializers.serialize("json", data)
  return StreamingHttpResponse(data)


