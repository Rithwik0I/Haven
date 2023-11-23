from django.shortcuts import render
from account.models import Account

# Create your views here.
def homescreenview(request):
    context = {}
    quest = Account.objects.all()
    context['quest'] = quest
    return render(request, "home.html", context)