from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from accountapp.models import Helloworld


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = Helloworld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = Helloworld.objects.all()
        return HttpResponseRedirect(reverse('accountapp: hello_world'))
    else:
        hello_world_list = Helloworld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})