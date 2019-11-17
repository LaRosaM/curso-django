from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me">Acerca de</a></li>
    <li><a href="/portafolio">Portafolio</a></li>
    <li><a href="/contacto">Contacto</a></li>
</ul>
"""


def home(request):
    return HttpResponse(html_base + """
        <h2>Portada</h2>
        <p>Esto es la portada</p>
    """)


def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo José y soy programador</p>
    """)


def portafolio(request):
    return HttpResponse(html_base + """
        <h2>Portafolio</h2>
        <p>Este es mi portafolio</p>
    """)


def contacto(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Mi contacto es el jose.larosa6@unmsm.edu.pe</p>
    """)
