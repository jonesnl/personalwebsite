from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.cache import cache_page

from frontpage.lastfm import pull_from_lastfm


@cache_page(60 * 2)  # cache for 2 minutes
def index(request):
    template = loader.get_template('frontpage/index.html')
    context = RequestContext(request, {
        'track_list': pull_from_lastfm(5),
    })
    return HttpResponse(template.render(context))
