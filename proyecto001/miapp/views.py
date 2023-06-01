from django.shortcuts import render, HttpResponse
# Create your views here.
layout = """
<h1> Proyecto Web (LP3) | Flor Cerdán </h1>
<hr/>
<ul>
<li>
<a href="/inicio"> Inicio</a>
</li>
<li>
<a href="/saludo"> Mensaje de Saludo</a>
</li>
<li>
<a href="/rango"> Mostrar Números [a,b]</a>
</li>
<li>
<a href="/rango2/10/15"> Mostrar Números [10,15]</a>
</li>
</ul>
<hr/>
"""

def index(request):
    mensaje="""
    <h1>Inicio</h1>
    """
    return HttpResponse(mensaje)
def saludo(request):
    mensaje = """
    <h1>Bienvenidos</h1>
    <h2>Flor Cerdán</h2>
    <h3>Python....</h3>
    """
    return HttpResponse(mensaje)
def rango2(request,a=0,b=100):
    a = 10
    b = 20
    resultado = f"""
        <h2> Numeros de [{a},{b}] </h2>
        Resultado: <br>
        <ul>
        """
    while a<=b:
        resultado += f"<li> {a} </li>"
        a+=1
        resultado += "</ul"
        return HttpResponse(resultado)
