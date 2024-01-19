from django import template

register = template.Library()

@register.filter(name='censor')
def censor(text):
    censored_words = [
        'аху', 'блядь', 'блять', 'мудак', 'мудила', 'гандон', 'долбоеб', 'чмо', 'сука', 'пидор', 'пидр', 'педик',
        'ебать', 'ебануться', 'ебал', 'еблан', 'залупа', 'хер', 'хуй', 'хуя', 'пизда', 'пиздеть', 'пиздюк', 'пиздюлина',
        'жопа', 'ёб', 'лох', 'суч', 'говно', 'говёный', 'говнюк', 'гондон', 'ебучий', 'ебан', 'залупа', 'манда', 'пизд',
        'срака', 'срать', 'трахаться', 'трахнуть', 'трахнул', 'трахнула', 'трах', 'хуёвый', 'хуёво', 'хуёвый', 'хули',
        'дроч', 'войн', 'мир', 'миру',
    ]
    for word in censored_words:
       if word in text:
          censored_word = word[0] + '*' * (len(word) - 1)
          text = text.replace(word, censored_word)
       elif word.capitalize() in text:
          censored_word = word[0].capitalize() + '*' * (len(word) - 1)
          text = text.replace(word.capitalize(), censored_word)
       elif word.upper() in text:
          censored_word = word[0].upper() + '*' * (len(word) - 1)
          text = text.replace(word.upper(), censored_word)

    return text