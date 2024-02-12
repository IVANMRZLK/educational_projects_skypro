from random import randint
import json
import requests
from basic_word import BasicWord

def load_random_word():
    words = requests.get('https://www.jsonkeeper.com/b/BHR2')
    # print(words.status_code)
    words = words.text
    words = json.loads(words)
    word = words[randint(0,len(words)-1)]
    w = BasicWord(word['word'],word['subwords'])
    return w

# print(load_random_word())

