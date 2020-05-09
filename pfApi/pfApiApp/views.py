from django.core.serializers import serialize
from django.http import HttpResponse

from .models import Label

# Create your views here.
def getLabels(request):
    data = serialize('json', Label.objects.all())
    return HttpResponse(data, content_type='application/json')
