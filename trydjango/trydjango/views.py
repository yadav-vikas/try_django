from django.http import HttpResponse


def home_view(request):
    HTML_STRING = "some text"
    return HttpResponse(HTML_STRING)