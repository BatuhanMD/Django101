from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
course_dic = {
    "python" : "Python Course Page",
    "java" : "Java Course Page",
    "c" : "C Course Page",
    "c++" : "C++ Course Page"
}

def course(request, item):
    return HttpResponse(course_dic.get(item,"Not Found!"))

def coursenum(request, num):
    course_list = list(course_dic.keys())
    try:
        course = course_list[num]
        page_to_go = reverse("course", args=[course])
        return HttpResponseRedirect(page_to_go)
    except:
        return HttpResponseNotFound("Not found!")

def index(request):
    return HttpResponse("First index: ")