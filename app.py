# -*- coding: utf-8 -*-
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from components.pages import pages

external_stylesheets = [dbc.themes.LUX]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "17rem",
    "padding": "2rem 1rem",
    "backgroundColor": "#f8f9fa",
}

CONTENT_STYLE = {
    "marginLeft": "17rem"
}

sidebar = html.Div(
    [
        html.H2("Censo Brasileiro 2010", className="display-5"),
        html.Hr(),
        html.P(
            "Uma interface para comparação de usabilidade das principais ferramentas de BI no mercado usando o censo brasileiro de 2010.", className="lead", style={'fontSize' : '15px'}
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home",            href="/page-1", id="page-1-link"),
                dbc.NavLink("Tableau Public",  href="/page-2", id="page-2-link"),
                dbc.NavLink("Power BI",        href="/page-3", id="page-3-link"),
                dbc.NavLink("Zoho Analytics",  href="/page-4", id="page-4-link"),
                dbc.NavLink("About",           href="/page-5", id="page-5-link")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

# this callback uses the current pathname to set the active state of the
# corresponding nav link to true, allowing users to see page they are on
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/":
        # Treat page 1 as the homepage / index
        return True, False, False
    return [pathname == f"/page-{i}" for i in range(1, 6)]

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/page-1"]:
        return pages['tableau']
    elif pathname == "/page-2":
        return pages['tableau']
    elif pathname == "/page-3":
        return pages['power_bi']
    elif pathname == "/page-4":
        return pages['zoho']
    elif pathname == "/page-5":
        return pages['zoho']
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
