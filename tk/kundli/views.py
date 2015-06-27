from django.shortcuts import render
from django.http import HttpResponse
import json
import requests
from requests_oauthlib import OAuth1
from mood import mood
import re
# Create your views here.

API_ID = 'KQRNLy8L4t8dQ4Loay0N1cGJV'
API_SECRET = 'lFi8oSsnR2NsHZUkArGFNx4IMa2unFTTxJm4zRWkC7fd9WlKKr'
OAUTH_TOKEN = '837804571-OORMT78jbTrbrgiLk2HYKIWyEblUuZN94PWub1pN'
OAUTH_TOKEN_SECRET = 'QMB9fvepUud1p8ykK68Ye3O0WfSzWeGfn9WQJbWhqJu08'

def index(request):
    return HttpResponse("Hello World")

TIMELINE_URI = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

def process(request):

    if request.GET:
        username = request.GET.get('username')
        payload = {'screen_name' : username, 'count' : 10}
        auth = OAuth1(API_ID, API_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

        r = requests.get(TIMELINE_URI,params=payload, auth=auth)

        abc = r.json()

        for i in abc:
            print i['text']
            re.sub(r'[^\x00-\x7F]+',' ', i['text'])
            print mood(i['text'])

        return HttpResponse("LOL")



    return HttpResponse("Oops")

