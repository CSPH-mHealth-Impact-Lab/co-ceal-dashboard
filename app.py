import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

from components.navbar import *
from components.filters import *

from dotenv import load_dotenv
import os

load_dotenv()

# Use the 'LUX' theme from Bootstrap for a clean, mobile-friendly design
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True)


app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/assets/custom.css'  # Path to your custom CSS file
        ),
    html.Script(
        src='/assets/script.js'  # Path to your JavaScript file
    ),  
    Navbar,
    show_hide_button,filter_container,
    dash.page_container,
])



if __name__ == '__main__':
    app.run_server(debug=True)


