import urwid


PASSWORD_LENGTH = 12
RATING_STEP = 2


def has_symbols(password: str) -> bool:
    return any(not symbol.isalnum() for symbol in password)


def has_lower_letters(password: str) -> bool:
    return any(symbol.islower() for symbol in password)


def has_upper_letters(password: str) -> bool:
    return any(symbol.isupper() for symbol in password)


def is_very_long(password: str) -> bool:
    return len(password) > PASSWORD_LENGTH


def has_digit(password: str) -> bool:
    return any(symbol.isdigit() for symbol in password)


def has_letters(password: str) -> bool:
    return any(symbol.isalpha() for symbol in password)


def rating_check(edit, password):
    rating = 0
    for check in rating_checks:
        if check(password):
            rating += RATING_STEP

    return reply.set_text(f'Рейтинг пароля: {rating}')


if __name__ == '__main__':
    rating_checks = (
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    )
    password = urwid.Edit('Введите пароль: ', mask='*')
    reply = urwid.Text("Рейтинг пароля: 0")
    menu = urwid.Pile([password, reply])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(password, 'change', rating_check)
    urwid.MainLoop(menu).run()
