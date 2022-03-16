import webbrowser
import os

"""
Single function to create a Dash app file. 
I'm not sure if this really saves any time or cognitive load since a template app file(the output of this function) is easier to read and edit as needed.
Especially since it relies on a helper function to create the datatable. I think its easier to clone this and replace as needed.
It was fun to make think through though.
"""


def create_dash(
    app_name: str,
    include_data: bool = False,
    open_app: bool = True,
    ext_css: str = None,
    theme: str = "BOOTSTRAP",
) -> None:

    # Create app file
    if app_name.__contains__(".py"):
        app_name = app_name.replace(".py", "")

    f = open(f"{app_name}.py", "w")

    # r = "static/style.css"

    f.writelines(
        [
            "from dash import Dash, html, dcc\n",
            "import dash_bootstrap_components as dbc\n",
            "from helpers import create_card\n",
            f"{('from helpers import load_data') if include_data else ''}\n\n",
        ]
    )

    if ext_css:
        f.writelines(
            [
                "dbc_css = 'static/style.css' # place additinoal css here\n",
                f"app = Dash(external_stylesheets=[dbc.themes.{theme.upper()}, dbc_css])\n\n",
            ]
        )
    else:
        f.writelines()
        f"app = Dash(external_stylesheets=[dbc.themes.{theme.upper()}])\n\n"

    # Import data (default to datatable)
    f.writelines([f"{('dt = load_data()') if include_data else ''}\n"])

    # Create app layout
    f.writelines(
        [
            "app.layout = html.Div(className='container',\n",
            "\tchildren=[html.H1(children='Hello Dash'),\n",
            "\n",
            "\thtml.Div(children='''\n",
            "\t\tReplace with application text\n",
            "\t'''),\n",
        ]
    )

    if include_data:
        f.writelines(
            [
                "\thtml.H1('Example Data Table'),\n",
                "\thtml.Div(dt, className='table'),\n",
            ]
        )

    f.writelines(["\thtml.Div(create_card('Example Card', )),\n"])    

    # Server code to run app
    f.writelines(
        [
            "]) # end layout\n\n",
            "\n",
            "if __name__ == '__main__':\n",
            "\tapp.run_server(debug=True)",
        ]
    )

    f.close()

    # run app
    if open_app:
        webbrowser.open("http://localhost:8050")
        os.system(f"python {app_name}.py")


if __name__ == "__main__":
    create_dash("test", include_data=True, open_app=True, ext_css=True, theme="materia")
