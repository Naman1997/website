from django.shortcuts import render

def general(request):
    return render(request, 'post_list.html', {})