from django.http import HttpResponse
from django.template import loader, RequestContext
from blog.models import Post, Author


def post(request, post_id):
    template = loader.get_template('blog/post.html')

    #Fill variables from database
    post = Post.objects.get(id=int(post_id))

    context = RequestContext(request, {
        'id': int(post_id),
        'title': post.title,
        'body': post.body,
        'created': post.created,
        'author_first': post.author.first_name,
        'author_last': post.author.last_name,
    })
    return HttpResponse(template.render(context))


def latest_post(request):
    post_id = Post.objects.order_by('-created')[0].id
    return post(request, post_id)
