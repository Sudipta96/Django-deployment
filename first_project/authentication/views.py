from django.shortcuts import render
from .forms import UserForm,UserProfileForm

# from django.contrib.auth import authenticate,login,logout
# from django.http import HttpResponseRedirect,HttpResponse
# from django.core import reverse
# from django.contrib.auth import login_required
# Create your views here.
def index(request):
    return render(request,'authentication/index.html')

def register(request):

    registered = False
    if request.method == 'POST':
        # user_form = UserForm(data=request.POST)
        # Create a form instance from POST data.
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():

            # Save a new Article object from the form's data.
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # Create, but don't save the new author instance.
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
             # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']
            registered = True
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request,'authentication/registration.html',
                                  {'user_form':user_form,
                                  'profile_form':profile_form,
                                  'registered':registered})

# def user_login(request):
#
#     if request.method=='POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username,password=password)
#
#         if user:
#             if user.is_active():
#                 login(request,user)
#                 return HttpResponseRedirect(reverse('index'))
#
#             else:
#                 return HttpResponse("Account not active")
#         else:
#             print("Someone tried to login and failed")
#             print("Username:{} and password {}".format(username,password))
#             return HttpResponse("invalid login details supplied")
#     else:
#
