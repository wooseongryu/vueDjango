def obj_to_post(obj, flag=True):
    """
    obj의 각 속성을 serialize해서, dict로 변환한다.
    serialize: python object -> (기본 타입) int, float, str
    시리얼라이즈는 파이썬 객체를 기본 타입으로 형 변환 해주는 과정이다.
    flag=True일 때는 /api/post/99/ 응답으로 모든 속성 다 보냄
    flag=False일 때는 /api/post/list/ 응답으로 일부 속성 만 보냄
    """
    # vars함수에는 ManyToMany필드는 들어있지 않다
    post = dict(vars(obj))

    if obj.category:
        # 오브젝트에에 category속성이 있는 경우에는 obj.category.name을 넣는다
        post['category'] = obj.category.name
    else:
        post['category'] = 'NoCategory'

    if obj.tags:
        post['tags'] = [t.name for t in obj.tags.all()]
    else:
        post['tags'] = []

    if obj.image:
        post['image'] = obj.image.url
    else:
        # 더미 이미지 생성하는 사이트
        post['image'] = 'https://via.placeholder.com/900x300'

    if obj.update_dt:
        # strftime함수는 datetime타입을 str타입으로 바꿔준다
        post['update_dt'] = obj.update_dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        post['update_dt'] = '9999-12-31 00:00:00'

    del post['_state'], post['category_id'], post['create_dt']
    if not flag:
        del post['tags'], post['update_dt'], post['description'], post['content']

    return post


def prev_next_post(obj):
    try:
        # 장고 Model.get_next_by_FOO 함수
        prevObj = obj.get_previous_by_update_dt()
        prevDict = {
            'id': prevObj.id,
            'title': prevObj.title,
        }
    except obj.DoesNotExist:
        prevDict = {}

    try:
        # 장고 Model.get_next_by_FOO 함수
        nextObj = obj.get_next_by_update_dt()
        nextDict = {
            'id': nextObj.id,
            'title': nextObj.title,
        }
    except obj.DoesNotExist:
        nextDict = {}

    return prevDict, nextDict
