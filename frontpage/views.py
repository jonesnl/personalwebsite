from django.http import HttpResponse
from django.template import RequestContext, loader, Context


def index(request):
    template = loader.get_template('base.html')
    context = Context()
    return HttpResponse(template.render(context))
