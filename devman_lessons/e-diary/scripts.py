import argparse
import os
import logging

from random import choice

import django
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from datacenter.models import (
    Schoolkid, Mark, Lesson, Commendation, Chastisement
)


PRAISES = [
        'Молодец!', 'Отлично!', 'Хорошо!', 'Сказано здорово – просто и ясно!',
        'Очень хороший ответ!', 'Талантливо!', 'Уже существенно лучше!',
        'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!'
]

def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()


def delete_chastisement(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()
        chastisement.save()


def create_commendation(schoolkid, discipline, text):
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=discipline
    ).order_by('-date')

    lesson = lessons.first()
    Commendation.objects.create(
        text=text,
        schoolkid=schoolkid,
        subject=lesson.subject,
        created=lesson.date,
        teacher=lesson.teacher
    )


def get_user_args():
    parser = argparse.ArgumentParser(
        description='Fix bad diary .'
    )
    parser.add_argument(
        '-n', '--full_name', help='Full name student'
    )
    parser.add_argument(
        '-s','--discipline', help='Item name'
    )
    parser.add_argument(
        '-m','--marks', action=argparse.BooleanOptionalAction,
        help='Fix marks'
    )
    parser.add_argument(
        '-d','--chastisement', action=argparse.BooleanOptionalAction,
        help='Delete_chastisement'
    )
    parser.add_argument(
        '-c','--commendation', action=argparse.BooleanOptionalAction,
        help='Create commendation'
    )

    args = parser.parse_args()

    return args


def main():
    args = get_user_args()

    text=choice(PRAISES)
    name = args.full_name
    discipline = args.discipline

    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)

    except ObjectDoesNotExist as erro:
        logging.error(f'Student not found: {erro}')

    except MultipleObjectsReturned as errm:
        logging.error(f'More than 1 student found: {errm}')

    if args.marks:
        fix_marks(schoolkid)

    if args.chastisement:
        delete_chastisement(schoolkid)

    if args.commendation:
        try:
            create_commendation(schoolkid, discipline, text)

        except ObjectDoesNotExist as erro:
            logging.error(f'Discipline not found: {erro}')


if __name__ == '__main__':
    main()