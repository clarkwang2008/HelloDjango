from django.http import HttpResponse
response = HttpResponse("Here is the text of the web page.")
response = HttpResponse("Text ONLY,PLEASE.", content_type="text/plain")
