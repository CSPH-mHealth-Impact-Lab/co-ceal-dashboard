import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

wave_1_3_title = html.Div([
    html.H1("Welcome to Your Dashboard for Change from Wave 1 to 3", className="my-custom-title text-center"),
])

wave_1_3_sub_title = html.Div([
    html.H1("We are working on the analysis! We will update this page shortly!", className="my-custom-title text-center"),
])

layout = html.Div([ 
    wave_1_3_title,
    wave_1_3_sub_title,
])