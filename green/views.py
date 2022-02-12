from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

from .models import *

def home(request):
    return render(request, 'green/Home.html')

def group(request):
    groups = Group.objects.all()
    return render(request, 'green/group.html', {'groups':groups})

def plant(request):
    plants=Plant.objects.all()
    return render(request, 'green/plant.html',{'plant':plant})

def shelf(request):
    cares = Care.objects.all()
    user = Care.user.filter(active = 1)
    return render(request, 'green/Shelf.html',{'cares':cares})

def login(request):
    user = User.objects.all()
    return render(request, 'green/Login.html', {'user':user})

def register(request):
    context = {}
    return render(request, 'green/Rejestracja.html',context)








class GroupView(generic.ListView):
    template_name = 'green/group.html'
    context_object_name = 'latest_qroup_list'

    def get_queryset(self):
        return Group.objects.order_by('name_gr')

class PlantView(generic.DetailView):
    model = Group
    template_name = 'green/detail.html'


class PlantsView(generic.ListView):
    template_name = 'green/plants.html'
    context_object_name = 'latest_plant_list'

    def get_queryset(self):
        return Plant.objects.order_by('name_pl')#[:5]

class ResultsView(generic.DetailView):
    model = Group
    template_name = 'green/results.html'

def like(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    try:
        selected_plant = group.plant_set.get(pk=request.POST['plant'])
    except (KeyError, Plant.DoesNotExist):
        # Redisplay the group water form.
        return render(request, 'green/detail.html', {
            'group': group,
            'error_message': "You didn't select a plant.",
        })
    else:
        selected_plant.likes += 1
        selected_plant.save()
        return HttpResponseRedirect(reverse('green:results', args=(group.id,)))

def loginPage(request):
    context = {}
    return render(request, 'green/login.html',context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'green/register.html', context)

class TestView(generic.ListView):
    template_name = 'green/test.html'
    context_object_name = 'latest_qroup_list'

    def get_queryset(self):
        return Group.objects.order_by('name_gr')


# def detail(request, group_id):
#     return HttpResponse("You're looking at group %s." % group_id)
#
#
# def results(request, group_id):
#     qroup = get_object_or_404(Group, pk=qroup_id)
#     return render(request, 'green/results.html', {'group': group})
#
#
# def index(request):
#     latest_qroup_list = Group.objects.order_by('name_gr')  # [:5]
#     context = {'latest_qroup_list': latest_qroup_list}
#     return render(request, 'green/index.html', context)

        
        
        
        
        
        
        
        
        
        
        
        