from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctorss
from .forms import BookingForm,ContactForm
from django.shortcuts import render, get_object_or_404
# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form ={
        'form' : form
    }
    return render(request,'booking.html',dict_form)

def doctors(request):
    doc_dict={
        'docs': Doctorss.objects.all()
    }
    return render(request,'doctors.html',doc_dict)

def contact(request):
    if request.method == "POST":
        formm = ContactForm(request.POST)
        if formm.is_valid():
            formm.save()
            return render(request,'confirmation1.html')
    formm = ContactForm()
    dict_formm ={
        'formm' : formm
    }
    return render(request,'contact.html',dict_formm)


def departments(request):
    dept_dict={
        'dept': Departments.objects.all()
    }
    return render(request,'departments.html',dept_dict)

def department_detail(request, id):
    department = get_object_or_404(Departments, id=id)
    return render(request, 'department_detail.html', {'department': department})



