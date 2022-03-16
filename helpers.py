import pandas as pd
from dash import dash_table, html
import dash_bootstrap_components as dbc

"""
Replace with own data or load from file/url
"""


def load_data():
    df = pd.DataFrame(
        {
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
        }
    )

    dt = dash_table.DataTable(
        df.head().to_dict("records"),
        id="tbl1",
        row_selectable="multi",
        sort_action="native",
    )
    return dt


def create_card(title: str = "Title", button_text: str = "Link"):
    card = dbc.Card(
        [
            dbc.CardImg(src="/static/images/placeholder.png", top=True),
            dbc.CardBody(
                [
                    html.H4(title, className="card-title"),
                    html.P(
                        "Some quick example text to build on the card title and "
                        "make up the bulk of the card's content.",
                        className="card-text",
                    ),
                    dbc.Button(button_text, color="primary"),
                ]
            ),
        ],
        style={"width": "18rem"},
    )
    return card


def list_bootstrap_themes():
    return print(
        "CERULEAN",
        "COSMO",
        "CYBORG",
        "DARKLY",
        "FLATLY",
        "JOURNAL",
        "LITERA",
        "LUMEN",
        "LUX",
        "MATERIA",
        "MINTY",
        "MORPH",
        "PULSE",
        "QUARTZ",
        "SANDSTONE",
        "SIMPLEX",
        "SKETCHY",
        "SLATE",
        "SOLAR",
        "SPACELAB",
        "SUPERHERO",
        "UNITED",
        "VAPOR",
        "YETI",
        "ZEPHYR",
        sep="\n",
    )
