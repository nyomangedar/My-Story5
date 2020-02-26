from django import forms
from .models import Friends, ClassYear
from django.forms import ModelForm

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friends
        fields = '__all__'





#class PostForm(forms.ModelForm):
 #   class Meta:
  #      model = Post
   #     fields = ("yourname", "classyear","hobby",)