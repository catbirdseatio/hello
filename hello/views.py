from django.http import HttpResponse
from django.views import View

data = []


class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello World!")
    
    def post(self, request):
        note = request.POST.get("note")
        data.append(note)
        return HttpResponse(data)