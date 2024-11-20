from django.shortcuts import render,redirect
from .models import Contract
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def contracts(request):
    if request.method == 'POST':
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        user_id=request.POST['user_id']
        
        #check if user has made inquiry already
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contracted=Contract.objects.all().filter(listing_id=listing_id,user_id=user_id)
            if has_contracted:
                messages.error(request,'you have already made an inquiry for this listings')
                return redirect('listings')
        
        contract=Contract(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contract.save()
        
        send_mail(
            'property Listing inquery',
            'There has been an inqury for '+listing + '.  sign into the admin panel for more details',
            'hasanyousuf.ml.django@gmail.com',
            ['yousufhasanrakib@gmail.com','akashhasanrakib3538@gmail.com','yousufhasan.ml.django@gmail.com'],
            fail_silently=False,
            
        )
        messages.success(request,'Your request has been submitted,a realtor will get back to you soon')
        return redirect('listings')
    
       
