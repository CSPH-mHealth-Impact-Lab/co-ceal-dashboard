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
    dbc.NavItem(dbc.NavLink("Wave 1", href="#", className="navbar-item active")),
    dbc.NavItem(dbc.NavLink("Wave 2", href="#", className="navbar-item active")),
    dbc.NavItem(dbc.NavLink("Wave 3", href="#", className="navbar-item active")),
    dbc.DropdownMenu(
        label="Cross Wave Analysis",  # Dropdown label
        children=[
            dbc.DropdownMenuItem("Option 4", href="#", className="navbar-item"),
            dbc.DropdownMenuItem("Option 5", href="#", className="navbar-item"),
            dbc.DropdownMenuItem("Option 6", href="#", className="navbar-item"),
        ],
    ),
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

Navbar = dbc.NavbarSimple(
        children=nav_items,
        brand="CO-CEAL DASHBOARD",
        brand_href="#",
        id="navbar",
        className="navbar navbar-expand-lg navbar-dark bg-dark p-1 m-1",
        )


app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/assets/custom.css'  # Path to your custom CSS file
        ),
    Navbar,
    filter_options,
    html.Div([
        html.H1("Welcome to Your Dash App", style={"text-align": "center", "color": text_color}),  # Use the hex color code for text color
        html.Div([
            html.Div([
                dcc.Graph(id="figure-1", className="figure"),
                dcc.Graph(id="figure-2", className="figure"),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="figure-3", className="figure"),
                dcc.Graph(id="figure-4", className="figure"),
                ], className="row-container"),
        ]),
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True)
