from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

def index(request):
    # render(request, 'love/index.html', {'errors': '无'})
    return render_to_response("love/index.html")
    return HttpResponse("Love ...")


# E:/Project/myFirstPro/app/templates/love/index.html
# E:\Project\myFirstPro\app\temlpates\love\index.html
