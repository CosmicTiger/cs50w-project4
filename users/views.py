from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from users.models import User
from primitiva_staff.models import Staff
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView
)
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import RegisterFormStepOne, RegisterFormStepTwo
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage
import os
from primitiva_project.settings import MEDIA_ROOT


# Create your views here.

def RegisterView(request):
    file_storage = FileSystemStorage(location=os.path.join(MEDIA_ROOT, 'staff_media'))

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        secondary_last_name = request.POST.get('secondary_last_name')
        profession = request.POST.get('profession')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        residence_city = request.POST.get('residence_city')

        user = User(username=username, email=email)
        user.set_password(password)
        user.save()

        staff = Staff(first_name=first_name, middle_name=middle_name, last_name=last_name,
                      secondary_last_name=secondary_last_name, profession=profession,
                      address=address, phone=phone, residence_city=residence_city, user= user)

        staff.save()

        user_authenticated = authenticate(username=user.username, password=password)
        login(request, user_authenticated)
        return redirect('dashboard_home')

    context = {
        'form_one': RegisterFormStepOne(),
        'form_two': RegisterFormStepTwo()
    }

    return render(request, "registration/register.html", context=context)
