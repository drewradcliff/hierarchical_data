from django.shortcuts import render

from app.models import File

def index(request):
    file_list = File.objects.all()
    return render(request, "index.html", {"file_list": file_list})