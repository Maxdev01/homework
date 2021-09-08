from django.shortcuts import render , redirect , get_object_or_404

from index.forms import AtikNouvoForm , UserForm

from django.contrib.auth import authenticate, login , logout  
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Atik


# Create your views here.


def indexpage(request):

    return render(request, 'index.html')


def li_atik(request, id):
    print(id)

    return render(request, 'atik-lekti.html')


@login_required(login_url='authentificate')
def atikNouvo(request):

    #get_article = get_object_or_404(Atik, slug=slug)
    if request.method == "POST":
        form = AtikNouvoForm(data=request.POST)
        if form.is_valid(): # si li valid
            tit = request.POST.get("tit")
            jounalis = request.POST.get("jounalis")
            kontni = request.POST.get('kontni')

            atik = Atik(tit=tit, jounalis=jounalis, kontni=kontni)
    
            atik.save()
            return redirect("detailpam")
        else:
            print("li pa valid")

    else:
        form = AtikNouvoForm()

    konteks = {"form": form}

    return render(request, 'article.html', konteks)


def authview(request):
    if request.method == "POST":
        form = UserForm(data= request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # my_user = User(username=data.get('username'))
            my_user = form.save(commit=False)
            my_user.set_password(data.get('password'))
            my_user.save()
            return redirect('connexion')
        
    else:
        form = UserForm()
    context = {'form': form}

    return render(request, 'signup.html', context)


def connecter(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
      
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('detailpam')
            
            

    else:
        form = UserForm()
        

    context = {'form': form}
    
    return render(request, 'connexion.html', context)


def dekonekte(request):

    logout(request)

    return redirect('first')