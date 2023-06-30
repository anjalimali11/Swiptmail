from django.shortcuts import render,HttpResponse,redirect
from messageapp.models import Msg
# Create your views here.
def student(request):
     #print("Request is:",request.method)
     if request.method=="GET":
        #print("In if section")
        return render(request,'student.html')

     else:
         #fetch data from the form
         n=request.POST['uname']
         mail=request.POST['uemail'] 
         mob=request.POST['mobile']
         rollno=request.POST['rollno']
         m.Msg(name=name,email=mail,mobile=mob,rollno=rollno)
         m.save()
         return redirect('/registration')

def registration(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'registration.html',context)

def delete(request,rid):
    m=Msg.objects.filter(id=rid)#fetchbthat object
    print(m)
    m.delete()
    return redirect('/registration')    
   
def edit(request,rid):

    if request.method=="GET":
        m=Msg.objects.filter(id=rid)
        #print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        upname=request.POST['uname']
        upemail=request.POST['uemail']
        upmob=request.POST['mobile']
        upmsg=request.POST['msg']
        #print(upname)
        #print(uemail)
        #print(upmob)
        #print(upmsg)
        return HttpResponse("Data is fetched")
        m=Msg.objects.filter(id=rid)
        m.update(name=upname,email=upemail,mobile=upmob,msg=upmsg)
        return redirect('/dashboard') 
