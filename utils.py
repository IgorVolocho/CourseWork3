import json


def get_posts_all(path='posts.json'):
    with open(path, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def get_posts_by_user(user_name):
    posts_found = []
    posts = get_posts_all()
    for post in posts:
        if post['poster_name'] == user_name:
            posts_found.append(post)
    if len(posts_found) == 0:
        raise ValueError('Пользователь не найден')
    else:
        return posts_found


def get_comments_by_post_id(post_id):
    comments_found = []
    comments = get_posts_all(path='comments.json')
    for comment in comments:
        if comment['post_id'] == post_id:
            comments_found.append(comment)
    if len(comments_found) == 0:
        raise ValueError('Пост не найден')
    else:
        return comments_found


def search_for_posts(query):
    posts_found = []
    posts = get_posts_all(path='posts.json')
    for post in posts:
        if query.lower() in post['content'].lower():
            posts_found.append(post)
    return posts_found


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post
