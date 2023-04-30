from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def firstview(request):
    s="Welcoe to Sunil Django Classes...Purely Nursely level classes"
    return HttpResponse(f"<h1>{s}</h1>")
