from django.shortcuts import render

def user_main_page(request):
    return render(
        request, "user_main_page.html", {}
    )