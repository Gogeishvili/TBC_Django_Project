from django.shortcuts import render

def user_main_page(request,user_id):
    return render(
        request, "user_main_page.html", {
            'user_id':user_id
        }
    )