import pytest
import json

import sys
sys.path.append('..')

from json import JSONDecodeError
from utils import path_comments, path_posts
from utils import get_posts_all, get_post_by_pk, get_posts_by_user, get_comments_by_post_id, get_comments_all, get_all_users, search_for_posts, get_all_post_pk

# path_comments = '../data/comments.JSON'
# path_posts = '../data/posts.JSON'
path_posts_comments_test = '../data/posts_comments_test.JSON'


with open(path_posts, 'r', encoding="utf-8") as file:
    posts = json.load(file)


with open(path_comments, 'r', encoding="utf-8") as file:
    comments = json.load(file)

leo_posts =[
  {
    "poster_name": "leo",
    "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
    "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
    "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
    "views_count": 376,
    "likes_count": 154,
    "pk": 1
  },{
    "poster_name": "leo",
    "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
    "pic": "https://images.unsplash.com/photo-1570427968906-5a309bfd7de3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=880&q=80",
    "content": "Пурр-пурр! типичная инстарамная фотка с котом , книжкой и едой. Но не буду скрывать, что это я: а то вдруг у вас кот тоже такой, тогда вы не увидите этого в своих фото. #кот #котики #инста #инстаграм #любовькживотным #любимыйкот ... Как же я люблю этот момент, когда ты понимаешь, что ты ничего толком не умеешь делать и даже не знаешь, что с этим делать.",
    "views_count": 287,
    "likes_count": 99,
    "pk": 5
  }
    ]

post_search ={
    "poster_name": "leo",
    "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
    "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
    "content": "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
    "views_count": 376,
    "likes_count": 154,
    "pk": 1
  }

comments_post_1 = [
  {
    "post_id": 1,
    "commenter_name": "hanna",
    "comment": "Очень здорово!",
    "pk": 1
  },
  {
    "post_id": 1,
    "commenter_name": "jlia",
    "comment": ":)",
    "pk": 2
  },
  {
    "post_id": 1,
    "commenter_name": "ralf",
    "comment": "Класс!",
    "pk": 3
  },
  {
    "post_id": 1,
    "commenter_name": "leo",
    "comment": "Интересно. А где это?",
    "pk": 4
  }]


#get_posts_all
def test_get_posts_all_normal():
    s = get_posts_all(path_posts)
    assert s == posts


def test_get_posts_all_JSONDecodeError():
    with pytest.raises(JSONDecodeError):
        get_posts_all(path_posts_comments_test)


def test_get_posts_all_FileNotFoundError():
     with pytest.raises(FileNotFoundError):
        get_posts_all('data/postss.json')

#get_comments_all
def test_get_comments_all_normal():
    s = get_posts_all(path_comments)
    assert s == comments


def test_get_comments_all_JSONDecodeError():
    with pytest.raises(JSONDecodeError):
        get_posts_all(path_posts_comments_test)


def test_get_comments_all_FileNotFoundError():
    with pytest.raises(FileNotFoundError):
        get_posts_all('data/possts.json')


#get_posts_by_user
def test_get_posts_by_user_normal():
    s = get_posts_by_user('leo')
    assert s == leo_posts

#Каким образом определить список пользователей?
def test_get_posts_by_user_empty_list():
    s = get_posts_by_user('ralf')
    assert s ==[]


def test_get_posts_by_user_ValueError():
    with pytest.raises(ValueError):
        get_posts_by_user('Борька')


#get_comments_by_post_id
def test_get_comments_by_post_id_normal():
    s = get_comments_by_post_id(1)
    assert s == comments_post_1


def test_get_comments_by_post_id_empty_post():
    s = get_comments_by_post_id(8)
    assert s == []


def test_get_comments_by_post_id_ValueError():
    with pytest.raises(ValueError):
        get_comments_by_post_id(100)

#search_for_posts
def test_search_for_posts_normal():
    s = search_for_posts("Ага, опять еда!")
    assert s == [post_search]


def test_search_for_posts_empty_post():
    s = search_for_posts('zxc')
    assert s == []


#get_post_by_pk
def test_get_post_by_pk_normal():
    s = get_post_by_pk(1)
    assert s == post_search


def test_get_post_by_pk_ValueError():
    with pytest.raises(ValueError):
        get_comments_by_post_id(100)



