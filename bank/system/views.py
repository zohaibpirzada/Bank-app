from django.shortcuts import render, redirect, get_object_or_404
from .models import profile, Transactions
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from django.forms import ModelForm
from time import sleep
from django.contrib.auth import login, logout, authenticate

class transaction_form(ModelForm):
    class Meta:
        model = Transactions
        fields = ['sender','reciver', "amount"]


def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            amount = request.POST['amount']
            sender = request.POST['sender']
            if sender != None and amount != None:
                # current_user = User.objects.get(username=request.user.username)
                current_user = get_object_or_404(User, username=request.user.username)
                if User.objects.filter(username=sender).exists():
                    if current_user == User.objects.get(username=sender):
                        messages.success(request, "You don't transfer yoursalf :-)")
                        return redirect('index')
                    else:
                        user_balance = profile.objects.get(user=request.user)
                        # print(add_user_balance.balance)
                        if int(amount) <= user_balance.balance:
                            return redirect('conform', sender=current_user, reciver=sender, send_amount=amount)

                        else:
                            messages.success(request, "Invalid Amount :-)")
                            return redirect('index')
                else:
                    messages.success(request, 'this user not exist :-)')
                    return redirect('index')
        user_transaction = Transactions.objects.all().order_by('-date')
        return render(request, 'index.html', {'transaction' : user_transaction})
    else:
        return redirect('login')

def money_transfer(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            amount = request.POST['amount']
            sender = request.POST['sender']
            current_user = User.objects.get(username=request.user.username)
            reciver = User.objects.get(username=sender)
            if sender != None and amount != None:
                if User.objects.filter(username=sender).exists():
                    if current_user == reciver:
                        messages.success(request, "You don't transfer yoursalf :-)")
                        return redirect('index')
                    else:
                        user_balance = profile.objects.get(user=request.user)
                        add_user_balance = profile.objects.get(user__username=sender)
                        # print(add_user_balance.balance)
                        if int(amount) <= user_balance.balance:
                            user_balance.balance = user_balance.balance-int(amount)
                            add_user_balance.balance = add_user_balance.balance+int(amount)
                            user_balance.save() 
                            add_user_balance.save()
                            sleep(4)
                            Transactions(sender=current_user, reciver=reciver ,amount=int(amount)).save()
                            messages.success(request, "Transfer Successfully :-)")
                            return redirect('index')
                        else:
                            messages.success(request, "Invalid Amount :-)")
                            return redirect('index')
                else:
                    messages.success(request, 'this user not exist :-)')
                    return redirect('index')
                    
            else:
                messages.success(request, 'Something wrong')
                return redirect('index')
        else:
            messages.success(request, 'Something wrong')
            return redirect('index')
    else:
        return redirect('login')
    
def conform(request, sender, reciver, send_amount):
    if request.user.is_authenticated:
        sender_user = get_object_or_404(profile, user__username=sender)
        reciver_user = get_object_or_404(profile, user__username=reciver)
        user_transaction = transaction_form(request.POST or None)
        return render(request, 'confrom.html', {'sender': sender_user, 'reciver' : reciver_user, 'send_amount' : send_amount, 'form' : user_transaction})
    else:
        return redirect('login')
    
def user_login(request):
    if request.user.is_authenticated:
        messages.success(request, 'You are already login!!')
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                messages.success(request, f'{username} was Successfully login!! Welcome')
                return redirect('index')
            else:
                messages.success(request, f'{username} Not Found!! Please Try Again')        
        return render(request, 'login.html')
    
def user_logout(request):
    logout(request)
    messages.success(request, f'Successfully logout')
    return redirect('login')

def Sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        phone = request.POST['phone']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.success(request, f'this User already exists')
                return redirect('sign')
            elif User.objects.filter(email=email).exists():
                messages.success(request, f'this email already exists')
                return redirect('sign')
            else:
                User.objects.create_user(username=username, password=password,email=email).save()
                user = authenticate(request, username=username, password=password)
                if user != None:
                    login(request, user)
                    if profile.objects.filter(phone_number=phone).exists():
                        messages.success(request, f'this Number already exists')
                        return redirect('sign')
                    else:
                        number = request.user.profile
                        number.phone_number = phone
                        number.save()
                    messages.success(request, f'{username} was Successfully Create!! Welcome')
                    return redirect('index')
        else:
            messages.success(request, f'Invalid Password')
            return redirect('sign')
    return render(request, 'sigin.html')

def transaction(request):
    user_transaction = Transactions.objects.all().order_by('-date')
    return render(request, 'transaction.html', {'transaction' : user_transaction})