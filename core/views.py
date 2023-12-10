from django.shortcuts import render, HttpResponse #crea respuestas http

# Create your views here.

"""
def home(request):
    return HttpResponse("<h1>Título</h1>")

def default(request):
    html_response = "<h1>Mensaje por defecto</h1>"

    for i in range(10) :
        #mostramos front mediante backend
        html_response+= "<h1>Mensaje por defecto</h1>"
        
    return HttpResponse(html_response)

    """

def portfolio(request):
    
    return render(request,"portfolio/portfolio.html")

