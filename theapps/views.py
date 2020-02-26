
from django.shortcuts import render
from django.http import HttpResponse
from .forms import FriendForm
from .models import Friends, ClassYear



def home (request):
    return render(request, 'story4.html')

def contact (request):
    return render(request, 'index-contact.html')

def thedata (request):
    data = Friends.objects.all()
    context = {'Data': data}
    return render(request, "data.html", context)

def forms(request):
    if request.method == 'POST':
        form = FriendForm(request.POST)
        if form.is_valid():
            data_item = form.save(commit=False)
            data_item.save()
            return render (request, 'form.html')
    else:
        form = FriendForm()
        return render (request, 'form.html', {'form' : form})





# #def form(request):
#  #   if request.method == 'POST':
#   #      form = FriendForm(request.POST)
#    #     if form.is_valid():
#     #        data_item = form.save(commit=False)
#             data_item.save()
#             return render(request, 'form.html')
#         else:
#             form = FriendForm()
#             return render(request, 'form.html', {'form': form})


#class FriendsView(TemplateView):
 #   template_name = 'form.html'

  #  def get(self,request):
   #     form = FriendsForm()
    #    return render(request, self.template_name, {'form': form})
    
   # def post(self, request):
    #    form = FriendsForm(request.POST)
     #   if form.is_valid():
      #      text = form.cleaned_data['fields']
       # args = {'form': form, 'text': text}
       # return render(request, self.template_name, args)





#def form (request):
 #   if request.method == "POST":
  #      form = FriendsForm(request.POST)
   #     if form.is_valid():
    #        post = form.save(commit=False)
     #       post.save()
      #      return redirect('form', pk=post)
    #else:
     #   form = FriendsForm()
    #return render(request, 'form.html', {'form':form})










#mhs_name = 'Nyoman'
#def form (request):
#
 #   persons = Person.objects.all().values()
#
 #   response = {'name': mhs_name, 'persons': persons}
  #  return render(request, 'form.html', response)

 




#def post_new(request):
 #   form = PostForm(request.POST)
  #  if request.method == "POST":    
   #     if form.is_valid():
    #        post = form.save(commit=False)
     #       post.author = request.user
      #      post.published_date = timezone.now()
       #     post.save()
        #    return redirect('post_detail', pk=post.pk)
       # else:
        #    form = PostForm()
    #return render(request, 'post_edit.html', {'form':form})
