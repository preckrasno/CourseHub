from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'hub/post_list.html', {})