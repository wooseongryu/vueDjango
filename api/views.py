from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from api.utils import obj_to_post, prev_next_post
from blog.models import Post


class ApiPostLV(BaseListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        # obj_to_post함수로 시리얼라이제이션을 함
        postList = [obj_to_post(obj, False) for obj in qs]
        # 최종 데이터를 JsonResponse로 클라이언트에 보낸다
        return JsonResponse(data=postList, safe=False, status=200)


class ApiPostDV(BaseDetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)

        jsonData = {
            'post': post,
            'prevPost': prevPost,
            'nextPost': nextPost,
        }
        return JsonResponse(data=jsonData, safe=True, status=200)
