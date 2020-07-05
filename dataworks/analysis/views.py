from django.shortcuts import render
from django.http import JsonResponse

from analysis.eda_gen import eda_csv

def data_analizer(request):
    req_met = request.method  # holds the request method
    host_val = request.META['HTTP_HOST']
    file_name = request.GET.get('file_name')  # getting the query strings passed in url
    data = eda_csv(file_name, host_val)
    return JsonResponse(data, safe=False)
