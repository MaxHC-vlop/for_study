import os

from collections import defaultdict
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

import pandas

from jinja2 import Environment, FileSystemLoader, select_autoescape
from dotenv import load_dotenv


CREATE_YEAR = 1920


def get_from_year_foundation_template() -> str:
    now_year = datetime.now().year
    difference_year = now_year - CREATE_YEAR
    last_numbers_year = difference_year % 100
    last_number_year = difference_year % 10

    if last_numbers_year in range(11, 21):
        cardinal_number = 'лет'
    else:
        if last_number_year == 1:
            cardinal_number = 'год'
        elif last_number_year in range(2, 5):
            cardinal_number = 'года'
        else:
            cardinal_number = 'лет'

    return f'{difference_year} {cardinal_number}'


def get_sorted_wine_map(filepath: str) -> dict:
    excel_data_df = pandas.read_excel(
        filepath,
        keep_default_na=False,
        )
    wine_collection = excel_data_df.to_dict('records')
    wine_map = defaultdict(list)

    for wine in wine_collection:
        category_wine_map = wine['Категория']
        wine_map[category_wine_map].append(wine)

        sorted_wine_map = {
            category_name: category_drinks for
            category_name, category_drinks in sorted(wine_map.items())
            }

    return sorted_wine_map


def make_index_page():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')

    rendered_page = template.render(
        wine_map=get_sorted_wine_map(),
        winery_age=get_from_year_foundation_template()
        )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


if __name__ == '__main__':
    load_dotenv()
    filepath = os.getenv('FILENAME')
    make_index_page()
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
