from django.shortcuts import render


def  register(request):
	return render(request,"register.html")
def login(request):
	return render(request,"login.html")
def home(request):
	return render(request,"home.html")

def about(request):
	return render(request,"about.html")
def contact(request):
	return render(request,"contact.html")

# # Create your views here.
# about.html
# contact.html
# index.html
# services.html
