from django.shortcuts import render


def homepage(request):
    return render(request, 'mailing_app/blog.html')
