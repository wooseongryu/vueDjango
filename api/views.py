from django.http import JsonResponse
from django.views.generic.list import BaseListView

from api.utils import obj_to_post
from blog.models import Post


class ApiPostLV(BaseListView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        # obj_to_post함수로 시리얼라이제이션을 함
        postList = [obj_to_post(obj) for obj in qs]
        # 최종 데이터를 JsonResponse로 클라이언트에 보낸다
        return JsonResponse(data=postList, safe=False, status=200)