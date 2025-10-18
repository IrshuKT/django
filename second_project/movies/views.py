from django.shortcuts import render ,redirect
from . models import Movie,Director,CensorInfo,Actor
from . forms import MovieForm,DirectorForm,CensorInfoForm,ActorForm

# Create your views here.

def index(request):
    movies_val = Movie.objects.all()
    return render(request,'index.html',{'values':movies_val})


def create(request):
    if request.POST:
       movieInfo = MovieForm(request.POST, request.FILES)
       if movieInfo.is_valid():
            movieInfo.save()
            return redirect('list')
    else:
        movieInfo = MovieForm()
    return render(request,'create.html',{'frm':movieInfo})


def list(request):
    movies_value = Movie.objects.all()
    return render(request,'list.html',{'movies':movies_value})

def edit(request,pk):
    edit_movie = Movie.objects.get(id=pk)
    if request.POST:
        frm =  MovieForm(request.POST,instance=edit_movie)
        if frm.is_valid():
            frm.save()
            return redirect('list')
    else:
          frm = MovieForm(instance=edit_movie)    
    return render(request,'create.html',{'frm':frm})

def delete(request,pk):
    delete_movie = Movie.objects.get(id=pk)
    
    delete_movie.delete()   
    movies_value = Movie.objects.all()
    return render(request,'list.html',{'movies':movies_value})



def director_list(request):
    directors = Director.objects.all()
    return render(request,'directors_list.html',{'director':directors})


def director(request):
    if request.POST:
       directorInfo = DirectorForm(request.POST, request.FILES)
       if directorInfo.is_valid():
            directorInfo.save()
            return redirect('list')
    else:
        directorInfo = DirectorForm()
    return render(request,'director.html',{'frm':directorInfo})



def censor_info(request):
    if request.POST:
       censorInfo = CensorInfoForm(request.POST, request.FILES)
       if censorInfo.is_valid():
            censorInfo.save()
            return redirect('list')
    else:
        censorInfo = CensorInfoForm()
    return render(request,'censor_info.html',{'frm':censorInfo})


def actor(request):
    if request.POST:
       actorInfo = ActorForm(request.POST, request.FILES)
       if actorInfo.is_valid():
            actorInfo.save()
            return redirect('list')
    else:
        actorInfo = ActorForm()
    return render(request,'actor.html',{'frm':actorInfo})   

def actor_list(request):
    actors = Actor.objects.all()
    return render(request,'actor_list.html',{'actor':actors})       
