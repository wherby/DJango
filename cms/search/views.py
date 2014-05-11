#from django.conf import settings
#settings.configure()
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.flatpages.models import FlatPage


def search(request):
    print "tesr"
    print FlatPage.objects
    query=request.GET.get('q','')
    keyword_results=[]
    results=[]
    if query:
        keyword_results=FlatPage.objects.filter(searchkeyword__keyword__in=query.split()).distinct()
        results=FlatPage.objects.filter(content__icontains=query)
    return render_to_response('search/search.html',
                              {'query':query,
                               'keyword_results':keyword_results,
                               'result':results})
