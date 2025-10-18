from django.forms import ModelForm
from .models import Movie, Director,CensorInfo,Actor


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class CensorInfoForm(ModelForm):
    class Meta:
        model = CensorInfo
        fields = '__all__'

class ActorForm(ModelForm):
    class Meta:
        model = Actor
        fields = '__all__'