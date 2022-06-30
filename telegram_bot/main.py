import os
import ptbot

from time import sleep
from dotenv import load_dotenv
from pytimeparse import parse


def get_value(chat_id, text_message):
    if type(parse(text_message)) == int:
        iteration = parse(text_message)
        message = 'Запускаю таймер ...'
        sleep(1)
        message_id = bot.send_message(chat_id, message)
        bot.create_countdown(
            parse(text_message),
            send_mail,
            iteration=iteration,
            chat_id=chat_id,
            message_id=message_id,
        )
        bot.create_timer(
            iteration,
            time_out,
            chat_id=chat_id,
            message_id=message_id
            )
    else:
        bot.send_message(chat_id, "Бот запущен")
        bot.send_message(chat_id, "На сколько запустить таймер?")


def send_mail(text_message, chat_id, message_id, iteration):
    message = f'Осталось {text_message} секунд\n'\
        f'{render_progressbar(iteration, text_message)}'
    bot.update_message(chat_id, message_id, message)


def time_out(chat_id, message_id):
    message = 'Время вышло'
    bot.update_message(chat_id, message_id, message)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.getenv('API_TOKEN')
    bot = ptbot.Bot(tg_token)
    bot.reply_on_message(get_value)
    bot.run_bot()
