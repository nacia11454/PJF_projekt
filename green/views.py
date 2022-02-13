from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect ,get_object_or_404
from django.urls import reverse
from .models import *
from .forms import UserForm

def home(request):
    return render(request, 'green/Home.html')

def group(request):
    groups = Group.objects.all()
    return render(request, 'green/group.html', {'groups':groups})

def group_pk(request,pk):
    groups = Group.objects.all()
    return render(request, 'green/group_pk.html', {'groups':groups})


def plant(request,pk):
    plant=Plant.objects.get(id = pk)
    return render(request, 'green/plant.html',{'plant':plant})

def shelf(request): #id jak brak to login
    cares = Care.objects.all()

    return render(request, 'green/Shelf.html',{'cares':cares})

def login(request):
    user = User.objects.all()
    return render(request, 'green/Login.html', {'user':user})

def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/green')

    context = {'form':form}
    return render(request, 'green/Rejestracja.html',context)

def log_out(request):
    user = User.objects.all()
    return render(request, 'green/log_out.html', {'user': user})



def test(request):
    return render(request, 'green/test.html')


# def like(request, group_id):
#     group = get_object_or_404(Group, pk=group_id)
#     try:
#         selected_plant = group.plant_set.get(pk=request.POST['plant'])
#
#         return render(request, 'green/detail.html', {
#             'group': group,
#             'error_message': "You didn't select a plant.",
#         })
#     else:
#         selected_plant.likes += 1
#         selected_plant.save()
#         return HttpResponseRedirect(reverse('green:results', args=(group.id,)))



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

        
        
        
        
        
        
        
        
        
        
        
        