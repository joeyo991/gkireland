from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserInfoForm


def profile(request):
    """ Displays Users' profiles """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserInfoForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Information updated successfully!')

    form = UserInfoForm(instance=profile)
    orders = profile.orders.all()

    template = 'user_profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
    }

    return render(request, template, context)
