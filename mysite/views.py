from django.shortcuts import render

# Home Page render
def home_page(request):
    return render(request,'base.html',{})

# About Page render
def about_page(request):
    return render(request,'about.html',{})

# Stage Page render 
def stage_page(request):
    return render(request,'stages.html',{})

# Exam Page render 
def exam_page(request):
    return render(request,'exam.html',{})

