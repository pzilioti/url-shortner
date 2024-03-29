from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from .models import Url
import hashlib


#Receives an URL, validates it and makes a shortend 5 characters version using the string's hash
def get_short_url(request):	
	url = request.GET.get('url')
	if(not url):
		return HttpResponse("Looks like your url is invalid, try a new one")

	validate = URLValidator()
	try:
		if(url[:4] != "http"):
			url = 'https://' + url
		validate(url)

		hash_object = hashlib.md5(bytes(url, 'utf-8'))
		short = hash_object.hexdigest()[:5]

		result = Url.objects.filter(short=short)
		if not result.exists():
			Url(short=short, long=url, click_count=0).save()

		return HttpResponse("Your shortned url is: " + request.build_absolute_uri('/' + short))
	except ValidationError as e:
		print(e)
		return HttpResponse("Looks like your url is invalid, try a new one")

#Receives a short URL and returns the original long url with the click count
def get_long_url(request):
	url = request.GET.get('url')
	if(not url or len(url) != 5):
		return HttpResponse("Please use the short url here")
	result = Url.objects.filter(short=url)
	if result.exists():
		return HttpResponse(result.get())
	else:
		return HttpResponse("This short url does not exists")

#Redirects to the original website while incrementing the click count
def redirect_url(request, url):
	if(len(url) != 5):
		return HttpResponse("Please use the short url here")
	result = Url.objects.filter(short=url)
	if result.exists():
		url = result.get()
		url.click_count = url.click_count + 1
		url.save()

		return redirect(url.long)
	else:
		return HttpResponse("This short url does not exists")


def index(request):
	return HttpResponse("Welcome, please use one of these endpoints: '/short/?url=(url)', '/long/?url=(short_url)', '/(short_url)'")