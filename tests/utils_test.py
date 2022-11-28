from Course3.utils import *


def test_get_posts_all():
    posts = get_posts_all(path='../posts.json')
    assert len(posts) != 0


def test_get_posts_all_1():
    posts = get_posts_all(path='../comments.json')
    assert len(posts) != 0

def test_get_posts_all_2():
    posts = get_posts_all(path='nothing.json')
    assert posts == FileNotFoundError


def test_get_posts_all_3():
    posts = get_posts_all(path='ava1.png')
    assert posts == FileNotFoundError


def test_get_posts_by_user():
    posts = get_posts_by_user('leo')
    assert len(posts) != 0


def test_get_posts_by_user_1():
    posts = get_posts_by_user('Mahmud')
    assert posts == 'Пользователь не найден'


def test_get_posts_by_user_2():
    posts = get_posts_by_user('johnny')
    assert len(posts) != 0




