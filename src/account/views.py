from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import SignUpForm, AccountAuthenticationForm, AccountUpdateForm

def signup_pageview(request):
    context ={}
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['signup_page'] = form
    else:
        form = SignUpForm()
        context['signup_page'] = form
    return render(request, 'makeacc.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")
    
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user =authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'login.html', context)

def account_view(request):

    if not request.user.is_authenticated:
        return redirect("login")
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )
    context['account_form'] = form
    return render(request, 'account.html', context)

# Create your views here.
