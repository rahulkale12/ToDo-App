from django.shortcuts import render,redirect
from app.models import ToDo

# Create your views here.
def read(request):
    reads = ToDo.objects.all().order_by('id')
    return render (request,"read.html", {'reads':reads})

def create(request):
    if request.method == "POST":
        to_do = request.POST['to_do']
        data = ToDo.objects.create(todo=to_do)
        data.save()
        return redirect('/read/')

    return render(request,"create.html")

def edit(request,id):
    edit_todo = ToDo.objects.get(id=id)
    return render(request,'edit.html',{'edit_todo':edit_todo})

def update(request,id):
    if request.method == "POST":
        to_do = request.POST['to_do']
        data1 = ToDo.objects.get(id=id)
        data1.todo = to_do
        data1.save()
        return redirect('/read/')
    
def delete(request,id):
    del_todo = ToDo.objects.get(id=id)
    del_todo.delete()
    return redirect('/read/')