import json


def get_post():
    '''Чтение файла с постами'''
    with open('data/data.json', 'r', encoding='utf-8') as f:
        posts = json.load(f)
    return posts


def get_comments():
    '''Чтение файла с комментариями'''
    with open('data/comments.json', 'r', encoding='utf-8') as f:
        comments = json.load(f)
    return comments


def get_post_pk(pk):
    '''Выборка по номера поста'''
    posts = get_post()
    for i in posts:
        if i['pk'] == pk:
            i['content'] = search_tag(i['content'])
            return i
    return None


def get_comment(pk):
    '''Выборка всех комментариев по определенному посту'''
    comments = get_comments()
    post_com = []
    for i in comments:
        if i['post_id'] == pk:
            post_com.append(i)
    return post_com


def get_comments_posts():
    '''Счетчик комментариев'''
    comments = get_comments()
    comments_dict = {}
    for i in comments:
        post_id = i['post_id']
        if post_id in comments_dict:
            comments_dict[post_id] += 1
        else:
            comments_dict[post_id] = 1
    return comments_dict


def post_search(word):
    '''поиск постов по словам'''
    post_search = []
    posts = get_post()
    for i in posts:
        if word in i['content'].lower():
            post_search.append(i)
    return post_search


def search_tag(word):
    '''поиск по тегам'''
    words = word.split(" ")
    for index, i in enumerate(words):
        if i.startswith("#"):
            tag = i[1:]
            link = f"<a href='/tag/{tag}'>{i}</a>"
            words[index] = link
    return ' '.join(words)

def tag(word):
    '''поиск по тегам'''
    words = word.split(" ")
    for index, i in enumerate(words):
        if i.startswith("#"):

            return i

def user_feed_dict(user):
    '''поиск постов по пользователю'''
    posts = get_post()
    user_feed = []
    for i in posts:
        if i['poster_name'] == user:
            user_feed.append(i)
    return user_feed



def count_views(pk):
    '''Счетчик просмотров'''
    with open('data/data.json', 'r+', encoding='utf-8') as f:
        posts = json.load(f)
        f.seek(0)
        for i in posts:
            if i['pk'] == pk:
                print(i)
            if i['pk'] == pk:
                i['views_count'] += 1
        json.dump(posts, f, indent=2, ensure_ascii=False)


# def bookmarks():
#     '''Читаем закладки'''
#     with open('data/bookmarks.json', 'r+', encoding='utf-8') as f:
#         bookmarks = json.load(f)
#
#     return bookmarks
#
# def add_bookmarks():
        '''Пытаемя записать закладки'''
#     with open('data/bookmarks.json', 'r+', encoding='utf-8') as f:
#         bookmarks = json.load(f)
#
#
#         json.dump(bookmarks, f, indent=2, ensure_ascii=False)
#     return bookmarks