#from django.conf import settings
#settings.configure()
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage


def search(request):
    print "tesr"
    print FlatPage.objects
    query=request.GET['q']
    return render_to_response('search/search.html',
                              {'query':query,
                               'result':FlatPage.objects.filter(content__icontains=query)})
