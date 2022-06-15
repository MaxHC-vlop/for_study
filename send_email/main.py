import os
import smtplib

import textwrap as tw

from dotenv import load_dotenv


def main():
    li = 'https://dvmn.org/referrals/bXWDB3z5QmCcBxLwUyteduEDeZgt5pOgSkiJwB3O/'
    friend_name = 'Владимир Владимирович'
    my_name = 'Владислав'
    message_text = '''
        Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

        %website% — это новая версия онлайн-курса по программированию.
        Изучаем Python и не только. Решаем задачи. Получаем ревью от
        преподавателя.

        Как будет проходить ваше обучение на %website%?

        → Попрактикуешься на реальных кейсах.
        Задачи от тимлидов со стажем от 10 лет в программировании.
        → Будешь учиться без стресса и бессонных ночей.
        Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и
        ровно столько, сколько можешь.
        → Подготовишь крепкое резюме.
        Все проекты — они же решение наших задачек — можно разместить на твоём
        GitHub. Работодатели такое оценят.

        Регистрируйся → %website%
        На модули, которые еще не вышли, можно подписаться и получить
        уведомление о релизе сразу на имейл.

    '''
    message_text = message_text.replace('%website%', li)
    message_text = message_text.replace('%friend_name%', friend_name)
    message_text = message_text.replace('%my_name%', my_name)

    email_from = 'mahxc@yandex.ru'
    email_to = 'mahxc@yandex.ru'
    letter = tw.dedent(f'''
        From: {email_from}
        To: {email_to}
        Subject: Приглашение!
        Content-Type: text/plain; charset="UTF-8";

        {message_text}

    ''').replace('\n', '', 1)
    letter = letter.encode('UTF-8')

    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login(login, password)
    server.sendmail(email_from, email_to, letter)
    server.quit()

if __name__ == '__main__':
    main()
