from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .forms import tour, tourform
from django.shortcuts import render, redirect, get_object_or_404
from .models import tour
from django.contrib.auth.decorators import login_required

list = []
form = tourform()


@login_required(login_url='/accounts/login')
def tour_create(request):
    user = request.user
    # houses_list = houses.objects.all().values_list('name', flat=True)

    if request.method == 'POST':
        form = tourform(request.POST, request.FILES)  # necessary if user wants to upload a picture
        if form.is_valid():
            instance = form.save(commit=False)  # lets us make some changes on the form before saving it on database
            instance.clas = user
            instance.pic = request.POST.get('image', False)

            #  return redirect(////)
            if instance.title in list:
                tours = tour.objects.filter(title=instance.title)
                tours.delete()
            instance.save()
            return redirect('tour:add')
    form = tourform()
    query = tour.objects.filter(clas=user)

    for tourww in query:
        list.append(tourww.title)

    return render(request, 'tour/addpage.html', {'form': form, 'tours_list': query})


def home_view(request):
    form = tourform()
    user = request.user
    query = tour.objects.all().values()

    return render(request, 'tour/home_page.html', {'form': form, 'tour_list': query})


def deletetour(request, pk):
    item = tour.objects.get(id=pk)
    item.delete()
    return redirect('tour:add')


def edittour(request, pk):
    tour_id = tour.objects.get(id=pk)
    form = tourform(instance=tour_id)

    if request.method == "POST":
        form = tourform(request.POST, instance=tour_id)
        if form.is_valid():
            form.save()
            return redirect('house:add')
    context = {'form': form}
    return render(request, 'tour/addpage.html', context)


def edandde(request):
    if 'edit' in request.POST:
        user = request.user
        students_list = tour.objects.all().values_list('name', flat=True)
        name = request.POST.get('tt')
        if name in list:
            tours = tour.objects.filter(title=name, cls=user)
            form = tourform(instance=tours)
            return redirect('tour:add')
        return redirect('tour:add')
    if 'delete' in request.POST:
        user = request.user
        if request.method == 'POST':
            name = request.POST.get('tt')
            tours = tour.objects.filter(title=name, clas=user)
            if tours.exists():
                tours.delete()
            return redirect('tour:add')
        return redirect('tour:add')
    return redirect('tour:add')
