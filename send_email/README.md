# Send email

This script allows you to send emails using the `smtplib` module. In addition, using the `dotenv` module allows you to hide secret data.

# How to start

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```bash
pip install -r requirements.txt
```

Create an .env file in your project directory and create 2 variables in that file:

```
LOGIN='user_email'
PASSWORD='user_password'
```

### Run

Launch on Linux(Python 3.5) or Windows as simple

```bash
$ python main.py
# You will see
$ python main.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)