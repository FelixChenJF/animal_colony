from django.http import HttpResponse
from django.template import loader
from .models import Mice

# Create your views here.
def home(request):
  mymice = Mice.objects.all().values()
  template = loader.get_template('home.html')
  context = {
    'mymice': mymice,
  }
  return HttpResponse(template.render(context, request))