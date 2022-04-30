from transliterate import translit
from num2words import num2words


text = '''
Ladies and gentlemen, I'm 78 years old and I finally got 15 minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.

More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When I was 8...
'''

numbers = (78, 15, 3, 40, 8)

def fedor_petrovich(phrase: str, numbers_in_phrase: tuple) -> None:
    print(translit(text, 'ru'))
    for num in numbers_in_phrase:
        print(num, '-',translit(num2words(num, lang='en'), 'ru'))


fedor_petrovich(text, numbers)
