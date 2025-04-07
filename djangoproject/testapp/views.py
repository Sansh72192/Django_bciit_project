from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request, 'testapp/home.html')
def faculty_view(request):
    return render(request,'testapp/faculty.html')
def students_view(request):
    return render(request,'testapp/student.html')
def event_view(request):
    return render(request,'testapp/events.html')