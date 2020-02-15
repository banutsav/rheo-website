from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, 'website/index.html', {})

# error page
def handler404(request, exception):
	return render(request, 'website/404.html', status=404)