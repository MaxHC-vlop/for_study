from transliterate import translit
from num2words import num2words


def translite_text(phrase: str) -> str:
    return translit(phrase, 'ru')


def translite_numbers(numbers_in_phrase: tuple) -> list:
    rec_fig = []
    for num in numbers_in_phrase:
        rec_fig += [str(num) + '-' + translit(num2words(num, lang='en'), 'ru')]
    return rec_fig


def main():
    text = '''
        Ladies and gentlemen, I'm 78 years old and I finally got 15 minut
        es of fame once in a lifetime and I guess that this is mine. Peop
        le have also told me to make these next few minutes escruciatingl
        y embarrassing and to take vengeance of my enemies. Neither will 
        happen.

        More than 3 years ago I moved to Novo-Novsk, but worked on new Magnetic
        Storage for last 40. When I was 8...

    '''
    numbers = (78, 15, 3, 40, 8)
    get_text = translite_text(text)
    get_numbers = translite_numbers(numbers)
    print(get_text, *get_numbers, sep='\n')

if __name__ == '__main__':
    main()
