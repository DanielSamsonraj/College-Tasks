from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Teacher, Post, Student
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
import random
from django.conf import settings

def index(request):
	return render(request, 'files/index.html')


def teacherRegistration(request):
	if request.user.is_authenticated:
		return redirect('viewPosts')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		confirm_password = request.POST['confirm-password']
		email = request.POST['email']
		name = request.POST['name']
		bio = request.POST['bio']
		subject = request.POST['subject']
		if password == confirm_password:
			try:
				checkUser = User.objects.get(username = username)
				messages.info(request, 'username already exists')
				return redirect('studentRegistration')
			except:
				user = User.objects.create_superuser(username = username, password = password)
				teacher = Teacher(user = user, email = email, name = name, bio = bio, subject = subject)
				teacher.save()
				response = auth.authenticate(username = username, password = password)
				if response:
					auth.login(request, user)
					messages.info(request,'Account created Successfully')
					return redirect('viewPosts')
				else:
					messages.info('There was an issue with login, Please try again')
					return redirect('teacherRegistration')
		else:
			messages.info(request, 'Password and Confirm Password should match')
			return redirect('teacherRegistration')
	return render(request, 'files/teacherRegistration.html')

def login(request):
	if request.user.is_authenticated:
		return redirect('viewPosts')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		response = auth.authenticate(username = username, password = password)
		if response:
			auth.login(request, response)
			return redirect('viewPosts')
		messages.info(request,"Invalid credentials please try again")
		return redirect('login')
	return render(request, 'files/Login.html')


@login_required(login_url='/login/')
def post(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			subject = request.POST['subject']
			topic = request.POST['topic']
			description = request.POST['description']
			link = request.POST['link']
			author = request.user
			postObj = Post(subject = subject, topic = topic, description = description, author = author, links = link)
			postObj.save()
			return HttpResponse("Posted Successfully")
		return render(request, 'files/uploads.html')
	return render(request, 'files/uploads.html')

def viewPosts(request):
	postObj = Post.objects.all()
	return render(request, 'files/Posts.html', {'PostData' : postObj})

	

def studentRegistration(request):
	if request.user.is_authenticated:
		return redirect('viewPosts')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		confirm_password = request.POST['confirm-password']
		email = request.POST['email']
		name = request.POST['name']
		bio = request.POST['bio']
		branch = request.POST['branch']
		year = request.POST['year']
		section = request.POST['section']
		if password == confirm_password:
			try:
				checkUser = User.objects.get(username = username)
				messages.info(request, 'username already exists')
				return redirect('studentRegistration')
			except:
				user = User.objects.create_user(username = username, password = password)
				studentObj = Student(user = user, email = email, name = name, bio = bio, branch = branch, year = year, section = section)
				studentObj.save()
				response = auth.authenticate(username = username, password = password)
				if response:
					auth.login(request, user)
					messages.info(request,'Account created Successfully')
					return redirect('viewPosts')
				else:
					messages.info('There was an issue with login, Please try again')
					return redirect('studentRegistration')

		else:
			messages.info(request, 'Password and Confirm Password should match')
			return redirect('studentRegistration')
	return render(request, 'files/studentRegistration.html')


def logout(request):
	auth.logout(request)
	return redirect('index')


def viewProfile(request):
	if request.user.is_superuser:
		userObj = Teacher.objects.all().filter(user = request.user)
	else:
		userObj = Student.objects.all().filter(user = request.user)
	for userDetails in userObj.values():
		details = userDetails
	return render(request, 'files/userProfile.html', details)

def OTP():
	return "".join([str(random.randrange(0,9)) for i in range(6)])
otp = 123456
def sendEmail(email):
	global otp
	otp = OTP()
	subject = "COLLEGE TASKS resetting password"
	from_email = settings.EMAIL_HOST_USER
	to_email = [email]
	signup_message = "Hey user," + '\n' + otp + " \n This is your OTP for your request" + '\n' + "If its not working please repeat this process again."
	send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently = False)

emailSendTo = "danielsam458@gmail.com"

def forgotPassword(request):
	global emailSendTo
	if request.method == 'POST':
		email = request.POST['email']
		user = Teacher.objects.all().filter(email = email)
		if user:
			sendEmail(email)
			emailSendTo = email
			return redirect('enterOTP')
		user = Student.objects.all().filter(email = email)
		if user:
			sendEmail(email)
			emailSendTo = email
			return redirect('enterOTP')
		else:
			messages.info(request, "There is no account with this email")
			return redirect('forgotPassword')
	return render(request, 'files/forgotPassword.html')

def enterOTP(request):
	global otp, emailSendTo
	if request.method == 'POST':
		OTP = request.POST['otp']
		if OTP == otp:
			return redirect('setPassword')
		else:
			messages.info(request, 'Invalid OTP')
			return redirect('enterOTP')
	return render(request, 'files/enterOTP.html', {'email' : emailSendTo})

def setPassword(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		confirm_password = request.POST['confirm-password']
		if confirm_password == password:
			user = User.objects.get(username = username)
			if user:
				user.set_password(password)
				user.save()
				messages.success(request, "You have changed the password succesfully please login with your new credentials")
				return redirect('login')
			else:
				messages.info(request, "There is no account with this username")
				return redirect('setPassword')
	return render(request, 'files/setPassword.html')