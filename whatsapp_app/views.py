from urllib import response
from django.shortcuts import render, HttpResponse
import os
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Create your views here.
@csrf_exempt
def home(request):
    message = client.messages.create( 
                              from_='whatsapp:+14783751065',  
                              body='Your Twilio code is 1238432',      
                              to='whatsapp:+919104540405' 
                          ) 
    return HttpResponse(message)


#14155238886