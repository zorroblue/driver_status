from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.template import RequestContext
from django.contrib import messages

from cab.models import *
from django.views.decorators.csrf import csrf_exempt
import hashlib


def display_drivers(request):
	#display the drivers
	#if request.method == 'GET':
	drivers = Driver.objects.all()
	return render(request, 'main.html',{'drivers' : drivers})

@csrf_exempt
def update_status(request):
	if request.method=='POST':
		number = request.POST.get('number')
		status = request.POST.get('status')
		print "The status ",status,number
		if status!=None and number!=None:
			driver = Driver.objects.get(driver_number = number)
			if driver!=None:
				Driver.objects.filter(driver_number__exact = number).update(status = status)
				return JsonResponse({'status': 'success'})
			else:
				return JsonResponse({'status':'fail'})
		else:
			return JsonResponse({'status' : 'fail'})

@csrf_exempt
def login(request):
	if request.method == 'POST':
		number = request.POST.get('number')
		password = request.POST.get('password')
		if number==None or password==None:
			return JsonResponse({'status' : 'fail'})
		else:
			# compute MD5 hash of password
			user = Driver.objects.filter(driver_number__exact = number)
			if len(user)==0:
				return JsonResponse({'status' : 'fail', 'reason':'No such user'})
			else:
				user = user[0]
				correct = user.password
				hashpass = hashlib.md5(password).hexdigest()
				if correct == hashpass:
					return JsonResponse({'status' : 'correct','reason' : 'Authenticated'})
				else:
					return JsonResponse({'status' : 'fail', 'reason' : 'Passwords dont match'})

@csrf_exempt
def register(request):
	if request.method == 'POST':
		number = request.POST.get('number')
		name = request.POST.get('name')
		password = request.POST.get('password')
		if number==None or name==None or password==None:
			return JsonResponse({'status':'fail', 'reason' : 'None values'})
		else:
			driver = Driver.objects.filter(driver_number__exact = number)
			if len(driver)!=0:
				#print driver
				#print driver[0].name,driver.driver_number
				return JsonResponse({'status':'fail', 'reason' : 'Already exists'})
			else:
				#register a new driver
				hashpass = hashlib.md5(password).hexdigest()
				driver = Driver(driver_number = number, name=name,password=hashpass,usesApp = True, status = "Free")
				driver.save()
				return JsonResponse({'status':'success'})