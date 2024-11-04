from django.shortcuts import render

def custom_404_view(request, exception=None):
    return render(request, '404.html', status=404)

def custom_500_view(request):
    raise Exception("This is a test error for the 500 page.")