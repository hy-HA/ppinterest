from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
# Create your views here.
from django.views.generic import CreateView

from accountapp.models import Helloworld


def hello_world(request):

    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = Helloworld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = Helloworld.objects.all()
        return HttpResponseRedirect
    else:
        hello_world_list = Helloworld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'
