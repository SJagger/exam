import io
import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import AddressBookList

@login_required
def home(request):
    contacts = AddressBookList.objects.all()
    return render(request, 'addressbook/home.html', {'title': 'Home', 'contacts':contacts})

@login_required
def create_contact(request):
    print(request.POST)
    fname = request.GET['fname']
    lname = request.GET['lname']
    cnumber = request.GET['cnumber']
    address = request.GET['address']
    contact_details = AddressBookList(fname=fname, lname=lname, cnumber=cnumber, address=address)
    contact_details.save()
    return redirect('/')

@login_required
def add_contact(request):
    return render(request, 'addressbook/add_contact.html')

@login_required
def delete_contact(request, id):
    contacts = AddressBookList.objects.get(pk=id)
    contacts.delete()
    return redirect('/')

@login_required
def edit_contact(request, id):
    contacts = AddressBookList.objects.get(pk=id)
    context = {
        'contacts' : contacts
    }
    return render(request, 'addressbook/edit_contact.html', context)

@login_required
def update_contact(request, id):
    contacts = AddressBookList.objects.get(pk=id)
    contacts.fname = request.GET['fname']
    contacts.lname = request.GET['lname']
    contacts.cnumber = request.GET['cnumber']
    contacts.address = request.GET['address']
    contacts.save()
    return redirect('/')

@login_required
def contact_upload(request):
    template = "addressbook/contact_upload.html"

    prompt = {
        'order': 'Order of the CSV should be FirstName, LastName, ContactNo, Address'
    }

    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        message.error(request, 'This is not a csv file', extra_tags='excel')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, quotechar="|"):
        _, created = AddressBookList.objects.update_or_create(
            fname=column[0],
            lname=column[1],
            cnumber=column[2],
            address=column[3]
        )

    context = {}
    return render(request, template, context)

@login_required
def contact_download(request):
    items = AddressBookList.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="contact.csv"'

    writer = csv.writer(response)
    writer.writerow(['FirstName', 'LastName', 'ContactNo', 'Address'])

    for obj in items:
        writer.writerow([obj.fname, obj.lname, obj.cnumber, obj.address])

    return response
