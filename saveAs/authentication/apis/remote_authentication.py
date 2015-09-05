from django.http import HttpResponse
from django.shortcuts import render
from saveAs.authentication.services import google_api
import requests

def google_authentication(request):
    print "trying to autheticate Google Drive"
    url = google_api.get_authorization_url('vibhor500@gmail.com', 'testing')
    print url
    response = requests.get(url)
    print response.text
    return HttpResponse("Success in authentication to Google Drive.")

def abc(request):
    access_token = request.GET["code"]
    user_info, credentials =  google_api.get_credentials(access_token, 'Test123')
    print user_info
    print "We have done it!!!!"

    result = google_api.get_file_list(credentials)
    print result
    return HttpResponse(result)
    #url = drive.get_authorization_url('neha.vibhor13@gmail.com', 'testing')
    #print url
    print google_api.get_credentials('4/ktu3Iok47KaXsISd3NDNsXaXGoxJ-OuC7a54OTRCQzo', 'Test123')
    return HttpResponse("Success in authentication to Google Drive.")

def abc(request):
    print request
    print "We have done it!!!!"
    return "Congrats"
