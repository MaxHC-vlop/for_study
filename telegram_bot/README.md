# Telegram bot

This bot can count seconds and show the end of the count as a percentage. Developed with `ptbot`, `pytimeparse`, `dotenv` libraries.

# How to start

Clone the repository with ssh:
```bash
git clone git@github.com:MaxHC-vlop/telegram_bot.git
```

Create a virtual environment on directory project:
```bash
python3.10 -m venv env
```

Start the virtual environment:
```bash
. env/bin/activate
```

Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```

Read [`this`](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html) manual
## Run

Create a file in the project directory `.env`:

![screen_here](./img/screen_vs.png)

Create `API_TOKEN` variable in `.env` file given by [BotFather](https://t.me/botfather):

```
API_TOKEN='SUPER_SECRET'
```

Launch on Linux(Python 3.10) or Windows as simple:

```bash
python3.10 main.py
# You will see
python3.10 main.py
```

You will see on telegram:
![screen_here](./img/screen_tl.png)