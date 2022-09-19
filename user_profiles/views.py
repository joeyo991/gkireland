from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserInfoForm


def profile(request):
    """ Displays Users' profiles """
    profile = get_object_or_404(UserProfile, user=request.user)

    form = UserInfoForm(instance=profile)
    orders = profile.orders.all()

    template = 'user_profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
