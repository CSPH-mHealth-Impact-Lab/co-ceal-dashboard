import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dotenv import load_dotenv
import os

load_dotenv()

# Use the 'LUX' theme from Bootstrap for a clean, mobile-friendly design
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Use environment variables for navbar background and text color
navbar_bg_color = os.environ.get('NAVBAR_BG_COLOR', '#RRGGBB')  # Default to your desired hex color code
text_color = os.environ.get('TEXT_COLOR', '#RRGGBB')  # Default to your desired hex color code

# Define the URLs for your logo images
logo1_url = "https://picsum.photos/seed/picsum/200/300"  # Replace with the URL of your first logo image
logo2_url = "https://picsum.photos/seed/picsum/200/300"  # Replace with the URL of your second logo image

nav_items = [
    dbc.NavItem(dbc.NavLink("Option 1", href="#", className="navbar-item")),
    dbc.NavItem(dbc.NavLink("Option 2", href="#", className="navbar-item")),
    dbc.NavItem(dbc.NavLink("Option 3", href="#", className="navbar-item")),
    dbc.NavItem(dbc.NavLink("Option 4", href="#", className="navbar-item")),
    dbc.NavItem(dbc.NavLink("Option 5", href="#", className="navbar-item")),
    dbc.NavItem(dbc.NavLink("Option 6", href="#", className="navbar-item")),
    dbc.NavItem(html.Img(src=logo1_url, height="50px"), style={'padding-right': '20px'}),
    dbc.NavItem(html.Img(src=logo2_url, height="50px")),
]

filter_options = html.Div([
    html.Div([
        html.Label("Filter 1"),
        dcc.Dropdown(
            id="filter-1",
            options=[
                {"label": "Option 1", "value": "option-1"},
                {"label": "Option 2", "value": "option-2"},
                {"label": "Option 3", "value": "option-3"},
                {"label": "Select All", "value": "select-all"},
            ],
            multi=True,
        ),
    ], className="filter"),
    
    html.Div([
        html.Label("Filter 2"),
        dcc.Dropdown(
            id="filter-2",
            options=[
                {"label": "Option 1", "value": "option-1"},
                {"label": "Option 2", "value": "option-2"},
                {"label": "Option 3", "value": "option-3"},
                {"label": "Select All", "value": "select-all"},
            ],
            multi=True,
        ),
    ], className="filter"),
    
    html.Div([
        html.Label("Filter 3"),
        dcc.Dropdown(
            id="filter-3",
            options=[
                {"label": "Option 1", "value": "option-1"},
                {"label": "Option 2", "value": "option-2"},
                {"label": "Option 3", "value": "option-3"},
                {"label": "Select All", "value": "select-all"},
            ],
            multi=True,
        ),
    ], className="filter"),
    
    html.Div([
        html.Label("Filter 4"),
        dcc.Dropdown(
            id="filter-4",
            options=[
                {"label": "Option 1", "value": "option-1"},
                {"label": "Option 2", "value": "option-2"},
                {"label": "Option 3", "value": "option-3"},
                {"label": "Select All", "value": "select-all"},
            ],
            multi=True,
        ),
    ], className="filter"),
], className="filter-container")



app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/assets/custom.css'  # Path to your custom CSS file
        ),
    dbc.NavbarSimple(
        children=nav_items,
        brand="CO-CEAL DASHBOARD",
        brand_href="#",
        style={"background-color": navbar_bg_color, "color": text_color},
        ),
    filter_options,
    html.Div([
        html.H1("Welcome to Your Dash App", style={"text-align": "center", "color": text_color}),  # Use the hex color code for text color
        html.Div([
            html.Div([
                dcc.Graph(id="figure-1"),
                dcc.Graph(id="figure-2"),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="figure-3"),
                dcc.Graph(id="figure-4"),
                ], className="row-container"),
        ]),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
