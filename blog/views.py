from django.views.generic import DetailView

from blog.models import Post


class PostDV(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
