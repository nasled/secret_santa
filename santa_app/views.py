from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import RegisterForm


def register(request):
    registered = False

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            name = request.POST.get("user_name", "")
            email = request.POST.get("user_email", "")

            user = User.objects.create_user(name, email, '')
            user.save()
            registered = True
    else:
        form = RegisterForm()

    return render(request, "register.html", {
        'form': form,
        'registered': registered
    })