from django.shortcuts import render


def profile(request):
    """ Displays Users' profiles """
    template = 'user_profiles/profile.html'
    context = {}

    return render(request, template, context)
