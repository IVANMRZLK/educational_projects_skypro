class Player:
    def __init__(self, us_name):
        self.us_name = us_name
        self.words_used_list = []

    def __repr__(self):
        return 'Пользователь ' + self.us_name

    def us_words_len(self): # получение количества использованых слов
        return len(self.words_used_list)

    def words_used_ap(self,us_word): # добавление слова в список использованных слов
        self.words_used_list.append(us_word)

    def usage_check_word(self, us_word): # проверка наличия введенного слова в списке использованных
        if us_word in self.words_used_list:
            return True
        else:
            return False