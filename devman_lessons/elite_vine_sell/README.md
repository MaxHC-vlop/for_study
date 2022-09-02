# Site for the sale of elite wine

Site for the sale of author's wine company "Новое русское вино". The site displays a list of drinks provided in the `beverages.xlsx` file.

File content:

Категория|Название|Сорт|Цена|Картинка|Акция
-|-|-|-|-|-
Белые вина|Белая леди|Дамский пальчик|399|belaya_ledi.png|Выгодное предложение

# How to start

Clone the repository with ssh:
```bash
git clone git@github.com:MaxHC-vlop/elite_vine_sell.git
```

Create a virtual environment on directory project (version Python3.10 or higher):
```bash
python3.10 -m venv env
```

Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```bash
pip install -r requirements.txt
```

Сreate a `.env` file and write in it which file to read data from:
```
FILENAME='your_file.xlsx'
```

## Run

```bash
python3.10 main.py
```

Go to website at : http://127.0.0.1:8000 , you will see :

![ddd](./images/screen.png)
