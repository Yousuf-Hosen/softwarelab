from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from listings.choices import price_choices,bedroom_choices,state_choices
# Create your views here.

def index(request):
    listings=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)

    context={'listings':paged_listings}
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context={
        'listing':listing
    }
    return render(request,'listings/listing.html',context)

def search(request):
    query_set=Listing.objects.order_by('-list_date')
    #keywords
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            query_set=query_set.filter(description__icontains=keywords)
    #city   
    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            query_set=query_set.filter(city__iexact=city)
            
    #state
    if 'state' in request.GET:
        state=request.GET['state']
        if state:
            query_set=query_set.filter(state__iexact=state)
    #bedroom
    if 'bedroom' in request.GET:
        bedroom=request.GET['bedroom']
        if bedroom:
            query_set=query_set.filter(bedroom__lte=bedroom)
    #price
    if 'price' in request.GET:
        price=request.GET['price']
        if price:
            query_set=query_set.filter(price__lte=price)
            
    
            
        
    context={
            'state_choices':state_choices,
             'bedroom_choices': bedroom_choices,
             'price_choices': price_choices,
             'listings':query_set,
             'values':request.GET
    }
    return render(request,'listings/search.html',context)

