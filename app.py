import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback_context, Input, Output, State
# from dash.dependencies import Input, Output, State

from components import filters, navbar,wave_1_components, wave_2_components, wave_3_components

from components.navbar import *
from components.filters import *
from custom_functions.custom_functions import *


from components.wave_2_components import *

from dotenv import load_dotenv
import os

load_dotenv()

filter_options = filter_options


# Use the 'LUX' theme from Bootstrap for a clean, mobile-friendly design
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], use_pages=True,
                suppress_callback_exceptions=True,
                )


app.layout = html.Div([dcc.Location(id='url', refresh=False),
    html.Link(
        rel='stylesheet',
        href='/assets/custom.css'  # Path to your custom CSS file
        ),
    html.Script(
        src='/assets/script.js'  # Path to your JavaScript file
    ),  
    html.P(id='my-output'),
    Navbar,
    show_hide_button,filter_container,
    dash.page_container,
])


server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)


