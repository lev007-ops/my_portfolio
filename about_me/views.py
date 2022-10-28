from django.shortcuts import render


def about_index(request):
    return render(request, 'about_me/about_index.html')
