from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserInfoForm
from checkout.models import Order


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


def order_history(request, order_number):
    """ Displays a past order from the order history """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is the confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
