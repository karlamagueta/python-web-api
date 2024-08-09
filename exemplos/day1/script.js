function python_rocks() {
    alert("Python Rocks!!");
}
logo_python = document.getElementsByTagName("img")[0]
logo_python.onclick = python_rocks;

function django_alert() {
    alert("Alerta DJANGO!!");
}
logo = document.getElementsByTagName("img")["logo_django"]
logo.onclick = django_alert;
