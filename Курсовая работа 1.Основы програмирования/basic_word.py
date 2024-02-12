class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return 'Слово ' + self.word

    def subwords_len(self): # подсчет количества подслов
        return len(self.subwords)

    def word_check(self,us_word): # проверка на наличие введенного слова в списке подслов
        if us_word in self.subwords:
            return True
        else:
            return False