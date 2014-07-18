from django.shortcuts import render

# Create your views here.

def index(request):
	pass




#API
def api(request):
	app = request.REQUEST.get("app")
	client = request.REQUEST.get("client")
	operation = request.REQUEST.get("op")
	detail = request.REQUEST.get("mode")

	pass


#INNER API FOR CODE GENERATION
def generator(request):
	app = request.REQUEST.get("app")
	os = request.REQUEST.get("os")
	namespace = request.REQUEST.get("ns")

	#os defines template

	#app defines strings

	#namespace defines dir structure and strings.

	
