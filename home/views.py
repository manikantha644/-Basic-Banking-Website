# from BasicBankingSystem import home

from django.shortcuts import render, redirect, HttpResponse
from django.db.models import F
from datetime import datetime

#create views

from .models import customer, transaction_details


def index(request):
    return render(request,'index.html')

def customers(request):
    all_entries = customer.objects.all()
    context = {
        "cust_details" : all_entries
    }
    return render(request, 'customers.html', context)

def customerid(request,customer_id):
        customeridd = customer.objects.get(account_no=customer_id)
        return render (request, "customerid.html",{
        "customeridd":customeridd,
        
        })
def search(request):
    query = request.GET['query']
    all_entries = customer.objects.filter(name__icontains=query)
    params= {"cust_details":all_entries}
    return render(request,'search.html',params)

def transaction(request):
    if request.method =="POST":
        receiver= request.POST.get('Transfer')
        money = request.POST.get('amountt')
        sender = request.POST.get('submit')  
        query1 = customer.objects.get(name= receiver)
        query1.amount= F('amount')+ money
        query1.save()
        query2 = customer.objects.get(name = sender)
        query2.amount= F('amount')- money
        query2.save()
        result = customer.objects.get(name = sender)
        transact = transaction_details()
        transact.source_name = sender
        transact.source_acc_no = result.account_no
        transact.Current_balance = result.amount
        transact.money_deposit = money
        transact.destination_name = receiver
        transact.date = datetime.today()
        transact.save()
        return redirect('customers')
    all_entries = transaction_details.objects.all()
    context = {
            "history" : all_entries
        }
    return render(request, 'transaction.html', context)

def view(request):
    if request.method == "POST":
         cust = request.POST.get('submit')
         query1 = customer.objects.get(name =cust)
         query2 = customer.objects.exclude(name = cust)
         context = {
             "cust_name" : query1,
             "all_details" : query2,
             }
         return render(request, 'view.html', context)


