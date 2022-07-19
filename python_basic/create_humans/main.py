import os
from random import choice, randint, sample

from faker import Faker

from file_operations import render_template


TEMPLATE_PATH = 'src/charsheet.svg'
CARDS_PATH = 'output/svg/'
CARD_NAME_TEMPLATE = 'result-{}.svg'
CARDS_QUANTITY = 10
MIN_CHOICE_NUM = 3
MAX_CHOICE_NUM = 18

SKILLS = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]

RUNE_ALPHABET = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}


def get_runic_skills(skills: list) -> list:
    runic_skills = []
    for skill in skills:
        for symbol in skill:
            skill = skill.replace(symbol, RUNE_ALPHABET[symbol])

        runic_skills += [skill]

    return runic_skills


def make_person_card() -> dict:
    fake = Faker("ru_RU")

    random_names = (
        (fake.first_name_male(), fake.last_name_male()),
        (fake.first_name_female(), fake.last_name_female())
    )
    first_name, last_name = choice(random_names)

    first_skill, second_skill, third_skill = \
        sample(get_runic_skills(SKILLS), 3)

    context = {
        'first_name': first_name,
        'last_name': last_name,
        'job': fake.job(),
        'town': fake.city(),
        'skill_1': first_skill,
        'skill_2': second_skill,
        'skill_3': third_skill,
        'strength': randint(MIN_CHOICE_NUM, MAX_CHOICE_NUM),
        'agility': randint(MIN_CHOICE_NUM, MAX_CHOICE_NUM),
        'endurance': randint(MIN_CHOICE_NUM, MAX_CHOICE_NUM),
        'intelligence': randint(MIN_CHOICE_NUM, MAX_CHOICE_NUM),
        'luck': randint(MIN_CHOICE_NUM, MAX_CHOICE_NUM)
    }

    return context


def main():
    os.makedirs(CARDS_PATH, exist_ok=True)

    end_path = CARDS_PATH + CARD_NAME_TEMPLATE
    for number_card in range(CARDS_QUANTITY):
        render_args = (
            TEMPLATE_PATH,
            end_path.format(number_card + 1),
            make_person_card()
        )

        render_template(*render_args)


if __name__ == '__main__':
    main()
