import dash
from dash import html, dcc, callback, Input, Output

dash.register_page(__name__)

wave_2_3_title = html.Div([
    html.H1("Welcome to Your Dashboard for Change from Wave 2 to 3", className="my-custom-title text-center"),
])

wave_2_3_sub_title = html.Div([
    html.H1("We are working on the analysis! We will update this page shortly!", className="my-custom-title text-center"),
])

layout = html.Div([ 
    wave_2_3_title,
    wave_2_3_sub_title,
])