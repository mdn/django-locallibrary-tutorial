
from django.shortcuts import render, redirect
from locallibrary.forms import PasswordUserCreationForm
from django.contrib.auth import login


def register_user(request):
    if request.method != 'POST':
        form = PasswordUserCreationForm()
    else:
        form = PasswordUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'registration/register_user.html', context)
