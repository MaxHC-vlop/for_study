# Обучение на Devman

Это учебный репозиторий .


## Домашнее задание по Знакомству с Python
---

Урок 1. Раскрутите планету:

* Запуск скрипта при помощи терминала:
  - Может пригодиться:
    - [Установка WSL для Windows](https://docs.microsoft.com/ru-ru/windows/wsl/install )
    - [Установка Python](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-programming-environment-on-an-ubuntu-18-04-server-ru)
```console
$python earth rotation.py
```

Урок 2. Готовим речь
```python
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
```