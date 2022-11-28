from Course3.main import *

def test_api_posts():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_api_post():
    response = app.test_client().get('/api/post/1')
    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert set(response.json.keys()) == {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
