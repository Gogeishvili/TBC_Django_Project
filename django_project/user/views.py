from django.shortcuts import render

# Create your views here.
def user_main_page(request):
    return render(
        request, "userMainPage.html", {}
    )