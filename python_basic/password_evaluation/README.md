# Password evaluation

The program assigns a rating from 0 to 12 to the password. Developed using the `urwid` library

# How to start

Clone the repository with ssh:
```bash
git@github.com:MaxHC-vlop/password_evaluation.git
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

## Run

Launch on Linux(Python 3.10) or Windows as simple:
```bash
python main.py
# you will see
Введите пароль: ▯
Рейтинг пароля: 0
```