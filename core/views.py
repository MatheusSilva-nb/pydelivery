from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cliente_page(request):
    return render(request, 'cliente.html')

def envio_page(request):
    return render(request, 'envio.html')