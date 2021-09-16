from django.shortcuts import render

# Create your views here.
def flight_list(request):
    return render(request, 'apicrud/flight_list.html')

def flight_detail(request, pk):
    context = {'pk':pk}
    return render(request, 'apicrud/flight_list', context)