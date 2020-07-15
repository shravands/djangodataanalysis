from django.shortcuts import render
from django.http import JsonResponse

from analysis.eda_gen import eda_csv

def data_analizer(request):
    req_met = request.method  # holds the request method
    host_val = request.META['HTTP_HOST']
    file_name = request.GET.get('file_name')  # getting the query strings passed in url
    if not file_name:
        return JsonResponse({"msg":"please pass the file name under argument file_name",
                             "example":"?file_name=file_name.csv"})
    elif not file_name.lower().endswith('.csv'):
        return JsonResponse({"msg":"The file is not of csv type"})
    else:
        data = eda_csv(file_name, host_val)
        return JsonResponse(data, safe=False)
