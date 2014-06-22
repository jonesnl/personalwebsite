from django.http import HttpResponse, Http404
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


def latest_posts(request, page_num=1):
    page_num = int(page_num)
    template = loader.get_template('blog/latest.html')

    page_num -= 1  # page numbers are based off 1, convert to based off 0 for database stuff

    if page_num < 0:
        raise Http404

    posts = Post.objects.order_by('-created')
    cur_page_posts = posts[(page_num*5):(page_num+1)*5]

    if len(cur_page_posts) <= 0:
        raise Http404

    if len(posts) > (page_num + 1) * 5:
        older_posts = True
    else:
        older_posts = False

    if page_num > 0:
        print(page_num)
        newer_posts = True
    else:
        print(page_num)
        newer_posts = False

    context = RequestContext(request, {
        'post_list': cur_page_posts,
        'page_num': page_num+1,
        'newer_posts': newer_posts,
        'older_posts': older_posts,
    })

    return HttpResponse(template.render(context))
