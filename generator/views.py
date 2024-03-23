from django.shortcuts import render
import random
# from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'randompassword1'})

def password(request):
    thepassword = ''

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if request.GET.get('special'):
        characters.extend(list('%$&/§$%&'))
    
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    
    length = int(request.GET.get('length', 12))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')



# mit request.GET.get('length') wird der name="length" aus der form abgegriffen (aus der home.html)
# alles was aus der <form> kommt, ist ein STRING !! Also, muss requested information aus "name"
# in einen int verwandelt werden (ab jetzt wird range(length) mit der length ermittelt, die in
# "name" in der Form angegeben wurde (also 6,7,8,9 Buchstaben). Mit get('length', 12) geht der
# default auf 12 Buchstaben für das Password, wenn kein Angabe in <form> über die "XX characters
# long" gemacht wird. 


# if request.GET.get('uppercase'):
#       characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
# Wenn in der <form> das input name="uppercase" geklickt ist, wird die list() mit den lowercase
# Buchstaben um die uppercase-Buchstaben erweitert


