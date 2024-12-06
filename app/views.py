from django.shortcuts import render

# Create your views here.
def enjoyments(request):
    return render(request,'enjoyments.html')

def Ticketbooking(request):
    return render(request,'Ticketbooking.html')