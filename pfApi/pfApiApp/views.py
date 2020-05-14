from django.core.serializers import serialize
from django.http import HttpResponse
import json

from .models import *
from .utils import  *

# Create your views here.
def getLabels(request):
    data = serialize('json', Label.objects.all())
    return HttpResponse(data, content_type='application/json')

def getMonthEntry(request, entryId):
    data = serialize('json', [MonthEntry.objects.get(pk = entryId)])[1:-1]
    return HttpResponse(data, content_type='application/json')

# TODO account for year
# TODO custom serializer to include label in json
def getMonthEntries(request, monthId, year):
    monthEntrySet = MonthEntry.objects.filter(entryDate__month = (monthId + 1)).order_by('entryDate')
    data = serialize('json', monthEntrySet)
    return HttpResponse(data, content_type='application/json')

# TODO account for year
def getMonthOverview(request, monthId, year):
    monthEntrySet = MonthEntry.objects.filter(entryDate__month = (monthId + 1))
    data = json.dumps(getMonthOverviewObject(monthEntrySet))
    return HttpResponse(data, content_type='application/json')
