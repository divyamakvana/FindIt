from django.shortcuts import render, redirect
from .models import ItemReport


# Create your views here.
def home(request):
    return render(request, "item/home.html")

def about(request):
    pass
def lost_item(request):
    items = ItemReport.objects.filter(report_type='LOST')
    return render(request, 'item/item_list.html' ,{'items': items, 'page_title': 'Lost Items', 'report_type': 'LOST'})


def found_item(request):
    items = ItemReport.objects.filter(report_type = 'FOUND')
    return render(request, 'item/found_item.html', {'items': items, 'page_title': 'Found Items', 'report_type': 'FOUND'})
    

def item_list(request):
    pass

def report_lost_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        description = request.POST.get('description')
        location = request.POST.get('location')
        ItemReport.objects.create(title=title, report_type='LOST', category=category, description=description, location=location)
        return redirect('lost_item')
    return render(request, 'item/report_form.html', {'page_title': 'Report Lost Item', 'report_type': 'LOST'})
