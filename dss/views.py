from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import dss.queries as query
# Create your views here.


#error message
msg = {"msg": "please give proper arguments"}


# views for combined logics start
def combined_index(request):
    data = {"results": {"value": "just for testing "}}
    return JsonResponse(data)

# a sample response for the customer request
def customers_data(request):
	data = query.all_customers()
	data_dict = data.to_dict('records')
	return JsonResponse(data_dict, safe= False)


# sample response to get the key passed in for the data 
def app_test(request):
    req_met = request.method  # holds the request method
    id = request.GET.get('id')  # getting the query strings passed in url
    data = {"results": {req_met: id}}
    return JsonResponse(data)


# example passing the keys example function
def key_pass(request, val, sec):
    the_key = (val * 1000)
    data = {"results": {the_key: sec, 'first_key': val, 'second_key':sec}}
    return JsonResponse(data)


# example function for validating the response on the get request 
def validated_response(request):
    id = request.GET.get('id')
    if id is None:
        return JsonResponse(msg)
    else:
    	req_met = request.method
    	data = {"results":{req_met: id}}
    return JsonResponse(data)