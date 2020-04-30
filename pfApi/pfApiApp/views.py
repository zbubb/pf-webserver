from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    test = {}
    test['name'] = 'Hello World'
    return JsonResponse(test)
