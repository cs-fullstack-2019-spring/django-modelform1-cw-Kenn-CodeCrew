from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogPostForm
from .models import BlogPostModel


# Create your views here.
def index(request):
    newForm = BlogPostForm()
    print(newForm)
    context = {
        "form": newForm
    }
    return render(request, "BlogPostApp/index.html", context)

def gotInfo(request):
    newEntry = BlogPostModel.objects.create(title = request.POST["title"], text = request.POST["text"])

    createHTMLLinkHome = "<br><br><a href='/'>Home</a>"
    return HttpResponse("Got that info" + createHTMLLinkHome)
