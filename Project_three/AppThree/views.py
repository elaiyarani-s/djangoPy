from django.shortcuts import render
from django.http import HttpResponse
from AppThree.models import AccessRecord,Topic,Webpage,UserProfile

# Create your views here.

def index(request):
    # return HttpResponse("<em>My Second App </em>")
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,"AppThree/index.html",context=date_dict)

def help(request):
    return render(request, 'AppThree/help.html')


