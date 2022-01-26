from django.shortcuts import render, redirect
from EcommerceApp.forms import UserForm, UserProfileForm
from EcommerceApp.models import UserProfile
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def signup(request):
    user = UserForm()
    cust = UserProfileForm()

    if request.method == 'POST':
        user = UserForm(request.POST)
        cust = UserProfileForm(request.POST)

        if user.is_valid() and cust.is_valid():
            userSaved = user.save()
            userSaved.set_password(userSaved.password)
            userSaved.save()

            custSaved = cust.save(commit=False)
            custSaved.user = userSaved
            custSaved.save()
            return HttpResponseRedirect('/signup/')

    return render(request, 'regisform.html', {'eform': cust, 'uform': user})


def login_call(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        userSelected = authenticate(username=username, password=password)
        if userSelected:
            login(request, userSelected)
            uData = UserProfile.objects.get(id=userSelected.id)
            if uData.usertype == 'Buyer':
                return redirect('/buyer/home/')
            if uData.usertype == 'Seller':
                return redirect('/seller/home/')
        else:
            return HttpResponse('<h1>Wrong Credentials...</h1>')
    else:
        return render(request, 'login.html')


@login_required
def logout_call(request):
    logout(request)
    return HttpResponseRedirect('/login/')
