import plotly.express as px


def plot(count):
    count = count or 1
    x = [str(i) for i in range(0, count)]
    y = list(range(0, count))
    return px.bar(x=x, y=y)


import dash
import dash_bootstrap_components as dbc
import flask
from dash import dcc, html

server = flask.Flask(__name__) # define flask app.server
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)

app.layout = html.Div(
    [
        dbc.NavbarSimple(brand="Dash - Slider with Plot Performance Test", color="primary", dark=True),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Slider(id="my-slider", min=1, max=50, step=1, value=10),
                    width=2,
                    style={"padding-top": "25px"},
                ),
                dbc.Col(dcc.Graph(id="example-graph", figure=plot(10)), width=10),
            ]
        ),
    ]
)


@app.callback(
    dash.dependencies.Output("example-graph", "figure"),
    [dash.dependencies.Input("my-slider", "drag_value")],
)
def update_plot(value):
    return plot(value)


if __name__ == "__main__":
    app.run_server(debug=True, port=80)
