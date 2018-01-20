from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.decorators.cache import cache_page
from django.utils.encoding import force_text

from frontpage.lastfm import pull_from_lastfm
from frontpage.models import Data


@cache_page(60 * 2)  # cache for 2 minutes
def index(request):
    template = loader.get_template('frontpage/index.html')
    context = {
        'front_body': Data.objects.get(key='front_body').value,
        'track_list': pull_from_lastfm(5),
    }
    return HttpResponse(template.render(context, request))
