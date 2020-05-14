from django.http import HttpResponse
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
import json

from .models import *
from .utils import  *

#TODO error handling
#TODO check for correct http request type
#TODO better csrf stuff

def getLabels(request):
    data = serialize('json', Label.objects.all())
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def createLabel(request):
    createLabelDto = json.loads(request.body)
    newLabel = Label(label_text = createLabelDto['label_text'])
    newLabel.save()
    data = serialize('json', [newLabel])[1:-1]
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def createMonthEntry(request):
    createEntryDto = json.loads(request.body)
    newEntry = MonthEntry(
            entryDate = createEntryDto['entryDate'],
            amount = createEntryDto['amount'],
            isPositive = createEntryDto['isPositive'],
            label = Label.objects.get(pk = createEntryDto['label'])
            )
    newEntry.save()
    entryId = newEntry.id
    data = serialize('json', [MonthEntry.objects.get(pk = entryId)])[1:-1]
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def editMonthEntry(request, entryId):
    updateEntryDto = json.loads(request.body)
    monthEntry = MonthEntry.objects.get(pk = entryId)
    monthEntry.entryDate = updateEntryDto['entryDate']
    monthEntry.amount = updateEntryDto['amount']
    monthEntry.isPositive = updateEntryDto['isPositive']
    monthEntry.label = Label.objects.get(pk = updateEntryDto['label'])
    monthEntry.save()
    data = serialize('json', [MonthEntry.objects.get(pk = entryId)])[1:-1]
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
