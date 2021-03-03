from django.shortcuts import render, HttpResponse

# Create your views here.


def app(request):
    return HttpResponse('This is the data & response')


def index(request):
    # return HttpResponse('This is Homepage(/)')
    context = {'name': 'harsha', 'course': 'Django'}
    return render(request, 'homepage.html', context)


def sampleapp(request):
    # Displays paths of all the blogspots inside the Django website
    # Fetch all the slugs from teh blog post table

    # context = {
    #     'heading': 'Django sample page using context - HEADING',
    #     'content': 'Django sample page using context - Content'

    # }

    return HttpResponse('This is the sample http response of view')


def about(request):
    # return HttpResponse('This is about page (/about)')
    return render(request, 'about.html')


def contact(request):
    # return HttpResponse('This is contact page (/contact)')
    return render(request, 'contact.html')


def projects(request):
    # return HttpResponse('This is projects page (/projects)')
    return render(request, 'projects.html')
