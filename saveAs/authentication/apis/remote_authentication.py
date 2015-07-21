from django.http import HttpResponse
from django.shortcuts import render
from saveAs.authentication.services import google_api
from apiclient import errors



def google_authentication(request):
    print "trying to autheticate Google Drive"
    #drive = GoogleDrive()
    url = google_api.get_authorization_url('vibhor500@gmail.com', 'testing')
    print url

    return HttpResponse("Success in authentication to Google Drive.")

def abc(request):
    access_token = request.GET["code"]
    user_info, credentials =  google_api.get_credentials(access_token, 'Test123')
    print user_info
    print "We have done it!!!!"

    result = google_api.get_file_list(credentials)
    print result
    return HttpResponse(result)
