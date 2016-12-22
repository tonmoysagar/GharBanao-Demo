from django.http import HttpResponse
from .models import Designers
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView
from django.core.urlresolvers import reverse_lazy
from .forms import UserForm
from django.views import View



def des_profiles(request,designerID):
    designer = get_object_or_404(Designers,designerID=designerID)

    return render(request,'designerPic/index.html',{'designer':designer})

class HomeView(generic.ListView):
    template_name = 'designerPic/Home.html'

    def get_queryset(self):
        return Designers.objects.all()

class DesignersCreate(CreateView):
    model = Designers
    fields = ['name','firmName','contact','img','password']


class DesignersUpdate(UpdateView):
    model = Designers
    fields = ['name','firmName','contact','img','password']

class UserFormView(View):
    form_class=UserForm
    template_name='designersPic/login.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user=authenticate(username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('designerPic/index.html', username)

        return render(request,self.template_name,{'form':form})





