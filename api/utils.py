def obj_to_post(obj):
    """
    obj의 각 속성을 serialize해서, dict로 변환한다.
    serialize: python object -> (기본 타입) int, float, str
    시리얼라이즈는 파이썬 객체를 기본 타입으로 형 변환 해주는 과정이다.
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
        post['image'] = 'https://via.placeholder.com/900x400'

    if obj.update_dt:
        # strftime함수는 datetime타입을 str타입으로 바꿔준다
        post['update_dt'] = obj.update_dt.strftime('%Y-%m-%d %H:%M:%S')
    else:
        post['update_dt'] = '9999-12-31 00:00:00'

    del post['_state'], post['category_id'], post['create_dt']

    return post
