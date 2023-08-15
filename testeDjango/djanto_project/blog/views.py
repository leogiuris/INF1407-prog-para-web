from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'leo',
        'title': 'blog post 1',
        'content':'First post content',
        'date_posted':'hoje'
    },
    {
        'author':'leo 2',
        'title': 'blog post 2',
        'content':'second post content',
        'date_posted':'amanhã'
    }
]


def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

