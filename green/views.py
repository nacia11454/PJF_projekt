from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect ,get_object_or_404
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .forms import UserForm, CareForm
from datetime import date


def registerPage(request):
    form = UserCreationForm()
    context = {'form':form}
    return render(request, 'green/Register.html', context)

def loginPage(request):
    users = User.objects.all()
    if request.method == "POST":

        name = request.POST.get('name')
        password = request.POST.get('password')

        user = users.filter(name_us = name, password = password)

        if user is not None:
            user.active = 1
            return redirect('/green')
        else:
            messages.info(request, 'Username OR password is incorrect')

        return redirect('/green/login')

    context = {}
    return render(request, 'green/Login.html', context)





def home(request):

    return render(request, 'green/Home.html')

def group(request):
    groups = Group.objects.all()
    return render(request, 'green/group.html', {'groups':groups})

def group_pk(request,pk):
    group = Group.objects.get(id = pk)
    context = {'group': group}
    return render(request, 'green/group_pk.html', context)

def plant(request,pk):
    plant = Plant.objects.get(id = pk)

    context = {'plant':plant}
    return render(request, 'green/plant.html',context)

def addPlant(request,pk):
    plant = Plant.objects.get(id = pk)
    user2 = User.objects.filter(name_us = "Adam")
    user = user2.first()
    care_date = date.today()
    new = Care(plant=plant, user=user, care_date=date.today(), note="x")

    form = CareForm(initial={'plant':plant, 'user':user, 'care_date':care_date })
    if request.method == 'POST':
        form = CareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/green/shelf/1' )

    context = {'form': form, 'plant':plant, 'user':user}
    return render(request, 'green/AddPlant.html',context)

def shelf(request,pk):
    users = User.objects.all()
    user = User.objects.get(id=pk)
    count = user.care_set.all().count()
    context = {'users':users, 'user': user, 'count':count}
    return render(request, 'green/Shelf.html',context)

def deletePlant(request, pk):
    care = Care.objects.get(id=pk)
    if request.method == "POST":
        care.delete()
        return redirect('/green/shelf/1' )


    context = {'care': care}
    return render(request, 'green/Delete.html',context)

def register2(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/green')

    context = {'form':form}
    return render(request, 'green/Rejestracja.html',context)

def log_out(request):
    users = User.objects.all()
    user = users.filter(active = 1)
    form = UserForm()
    countUs = user.count()
    if countUs == 0:
        return render(request, 'green/login.html')
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user.active = 0
            form.save()
            return redirect('/green')

    context = {'form': form}
    return render(request, 'green/log_out.html', context)






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

        
        
        
        
        
        
        
        
        
        
        
        