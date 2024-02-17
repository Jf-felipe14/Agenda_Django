from django.shortcuts import render,get_object_or_404,redirect
from .models import Contact
from django.db.models import Q
from django.core.paginator import Paginator


def page(request):
    contacts = Contact.objects.all().order_by('-id')
    paginator = Paginator(contacts,25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    con={
        'page_obj':page_obj
    }
    return render(request,'index.html',context=con)


def single_page(request,id:int):
    # single_contact=Contact.objects.get(pk=id)
    single_contact=get_object_or_404(Contact,pk=id,show=True)
    con1={
        'contact':single_contact
    }
    return render(request,'contact.html',context=con1)

def search(request):
    search_value=request.GET.get('q','').strip()
    if search_value  == '':
        return redirect('contact:index')
    contacts=Contact.objects.all().filter(Q(first_name__icontains=search_value) | 
                                        Q(last_name__icontains=search_value) |
                                        Q(phone__icontains=search_value) |
                                        Q(email__icontains=search_value) |
                                        Q(id__icontains=search_value))\
                                        .order_by('-id')
    paginator=Paginator(contacts,25)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    con={
        'page_obj':page_obj,
        'search_value':search_value
    }
    print(contacts.query)
    return render(request,'index.html',context=con)


def create(request):
    
    con={
        
    }
    return render(request,'create.html',context=con)