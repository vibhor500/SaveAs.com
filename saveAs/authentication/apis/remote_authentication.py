from django.http import HttpResponse
from django.shortcuts import render
from saveAs.authentication.services import google_api

def google_authentication(request):
    print "trying to autheticate Google Drive"
    #drive = GoogleDrive()
    #url = drive.get_authorization_url('neha.vibhor13@gmail.com', 'testing')
    #print url
    print google_api.get_credentials('4/ktu3Iok47KaXsISd3NDNsXaXGoxJ-OuC7a54OTRCQzo', 'Test123')
    return HttpResponse("Success in authentication to Google Drive.")

def abc(request):
    print request
    print "We have done it!!!!"
    return "Congrats"
