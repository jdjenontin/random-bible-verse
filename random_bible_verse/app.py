import dash
import dash_bootstrap_components as dbc
from dash import html, callback, Input, Output, dcc

from random_bible_verse.crud_bible import get_random_verse_from_version

from random_bible_verse.config import settings

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Random Bible Verse",
    )

server = app.server

app.layout = dbc.Container(
    [
        html.H1("Random Bible Verse", className="text-center border-bottom border-primary pb-4 mb-4"),
        html.H2(id="verse-text", className="text-center"),
        html.H2(id="verse-reference", className="text-center border-top border-primary pt-4 mt-4"),

        dcc.Interval(id="interval", interval=settings.REFRESH_INTERVAL_MS, n_intervals=0),
    ],
    class_name="d-flex flex-column justify-content-center align-items-center vh-100",
)

@callback(
    Output("verse-text", "children"),
    Output("verse-reference", "children"),
    Input("interval", "n_intervals"),
)
def update_verse(_):
    verse = get_random_verse_from_version(settings.BIBLE_VERSION)
    if verse:
        return verse.verse_text, verse.reference
    else :
        return "Error", "Error"


if __name__ == "__main__":
    app.run_server(debug=True)