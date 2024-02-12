from basic_word import BasicWord
from player import Player
from utils import load_random_word

user_name = input(f'Введите имя игрока: ')
player = Player(user_name)
word = load_random_word()

print(f'Привет, {user_name}!')
print(f'Составьте {word.subwords_len()} слов(а) из слова "{word.word}"')
print(f'Чтобы закончить игру, угадайте все слова или напишите "stop"')

player_word = input(f'Поехали, ваше первое слово?\n')
player_word = player_word.lower()
a = 0

while len(player.words_used_list) != len(word.subwords):
    if a != 0:
        player_word = input(f'Cлово?\n')
    else:
        a += 1

    if len(player_word) < 3:
        print('Слишком короткое слово.')
        continue
    elif player_word == 'stop' or player_word == 'стоп':
        break
    elif player_word not in word.subwords:
        print('Неверное слово.')
        continue
    elif player_word in player.words_used_list:
        print('Это слово уже было угадано.')
        continue
    else:
        print('Верно!')
        player.words_used_list.append(player_word)
        continue

print(f'Игра завершена. Вы угадали {len(player.words_used_list)} слов из {word.subwords_len()}')




