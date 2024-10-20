from django.shortcuts import render

def user_main_page(request):
    return render(
        request, "userMainPage.html", {}
    )