from django.shortcuts import render

from osmapi import OsmApi

from django.conf import settings

# Create your views here.

def index(request):
	return render(request, "index.html")

def app_page(rquest, app_id):
	return render(request, "app.html")


#API

def app_stats(request, app_id):
	pass

def login(request):
	userid = request.REQUEST.get("user")
	password = request.REQUEST.get("password")
	pass

def api(request):
	app = request.REQUEST.get("app")
	client = request.REQUEST.get("client")
	operation = request.REQUEST.get("op")
	mode = request.REQUEST.get("mode")
	data = request.REQUEST.get("data", {"none":None})
	if not all([app,client,operation, mode, data]):
		return 

	MyApi = OsmApi.OsmApi(username = settings.get("osm_user"), password = settings.get("osm_pass"))
	
	if operation == "write":
		MyApi.ChangesetCreate({u"comment": u"OsmApp Upload"})



		MyApi.ChangesetClose()

	else:
		OVERPASS_STRING="""
			<osm-script output="json" timeout="25">
			  <!-- gather results -->
			  <union>
			    <!-- query part for: "vending=condoms" -->
			    <query type="node">
			      <has-kv k="vending" v="condoms"/>
			      <bbox-query {{bbox}}/>
			    </query>
			    <query type="way">
			      <has-kv k="vending" v="condoms"/>
			      <bbox-query {{bbox}}/>
			    </query>
			    <query type="relation">
			      <has-kv k="vending" v="condoms"/>
			      <bbox-query {{bbox}}/>
			    </query>
			  </union>
			  <!-- print results -->
			  <print mode="body"/>
			  <recurse type="down"/>
			  <print mode="skeleton" order="quadtile"/>
			</osm-script>
		"""
	
	pass


#INNER API FOR CODE GENERATION
def generator(request):
	app = request.REQUEST.get("app")
	os = request.REQUEST.get("os")
	namespace = request.REQUEST.get("ns")

	#os defines template

	#app defines strings

	#namespace defines dir structure and strings.


