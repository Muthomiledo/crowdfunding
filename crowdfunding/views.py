from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Campaign
from django.views import View


def home(request):
    campaigns = Campaign.objects.all()
    return render(request, 'home.html', {'campaigns': campaigns})

class CampaignDetail(View):
    def get(self, request, pk):
        campaign = get_object_or_404(Campaign, pk=pk)
        return render(request, 'campaign_detail.html', {'campaign': campaign})

def make_donation(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    if request.method == 'POST':
        amount = request.POST['amount']
        campaign.current_amount += float(amount)
        campaign.save()
        return render(request, 'donation_success.html', {'campaign': campaign, 'amount': amount})
    else:
        return render(request, 'make_donation.html', {'campaign': campaign})

def create_campaign(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        goal_amount = request.POST['goal_amount']
        end_date = request.POST['end_date']
        campaign = Campaign(title=title, description=description, goal_amount=goal_amount, end_date=end_date)
        campaign.save()
        return render(request, 'campaign_success.html', {'campaign': campaign})
    else:
        return render(request, 'create_campaign.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if not (username and email and password and confirm_password):
            return render(request, 'register.html', {'error': 'Please fill in all required fields'})
        elif password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'register.html')
