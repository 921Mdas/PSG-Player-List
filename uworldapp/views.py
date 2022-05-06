from ast import Delete
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Player, Photo
from uworldapp.forms import seeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView, FormView, DeleteView, UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import connection

import uuid
import boto3
S3_BASE_URL = 'https://s3.ca-central-1.amazonaws.com/'
BUCKET = 'rodeopsg921'

# Create your views here.

# we can render detailed data here truncate
def home(request):
    return render(request, "home.html")

class createPlayer(CreateView):
    model = Player
    template_name="create_player.html"
    fields =['name','language','position','score']
    success_url = ('/allplayers/')
    
# generate a basic form with class based view
class myForm(FormView):
    template_name = 'contact.html'
    form_class = seeForm
    success_url ='/about/'
    
    def form_valid(self, form):
        form.send_email()
        if(super().form_valid(form)):
            HttpResponse('form is valid')
        else:
            HttpResponse('form is invalid')
        return super().form_valid(form)

# truncate data here using queryset instead of passing the whole db
class ShowPlayers(ListView):
    model = Player
    template_name='all_players.html'
    context_object_name = 'soccer_players'
    queryset = Player.objects.all()
    # queryset = Player.objects.order_by("-language")
    # queryset = Player.objects.filter(position="striker")
    
# see one player
def OnePlayer(request,idx):
    player = Player.objects.get(id=idx)
    return render(request, "edit.html", {'player':player})

class DeletePlayer(DeleteView):
    model = Player
    success_url=reverse_lazy("players")
    template_name='uworldapp_app/player_confirm_delete.html'

class UpdatePlayer(UpdateView):
    model = Player
    fields = ['name','language','position']
    template_name = "update_form.html"
    success_url=reverse_lazy("players")

# just rendering a template without passing data
class About(TemplateView):
    template_name = 'about.html'

def add_photo(request, player_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, player_id=player_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('players')

    # return redirect('detail', player_id=player_id)

class weather(APIView):
    def get(self,request):
        cursor = connection.cursor()
        cursor.execute("SELECT * from weahter")
        results = cursor.fetchall()
        keys = ["id","month","rain","lowest"]
        final =[]
        for result in results:
            pet = {}
            for idx in range(len(result)):
               pet[keys[idx]]= result[idx]
            final.append(pet)
        # columns = [col[1] for col in results]
        return Response(final)
