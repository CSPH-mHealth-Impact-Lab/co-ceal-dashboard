import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

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
    dbc.NavItem(dbc.NavLink("Wave 1", href="#")),
    dbc.NavItem(dbc.NavLink("Wave 2", href="#")),
    dbc.NavItem(dbc.NavLink("Wave 3", href="#")),
    dbc.DropdownMenu(
        label="Cross Wave Analysis",  # Dropdown label
        children=[
            dbc.DropdownMenuItem("Option 4", href="#"),
            dbc.DropdownMenuItem("Option 5", href="#"),
            dbc.DropdownMenuItem("Option 6", href="#"),
        ],
    ),
]

Navbar = dbc.NavbarSimple(
        children=nav_items,
        brand="CO-CEAL DASHBOARD",
        brand_href="#",
        id="navbar",
        className="navbar navbar-expand-lg navbar-dark bg-dark p-1 m-1",
    )

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

wave_1_demographic_figures = html.Div([
            html.Div([
                dcc.Graph(id="figure-1", className="figure"),
                dcc.Graph(id="figure-2", className="figure"),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="figure-3", className="figure"),
                dcc.Graph(id="figure-4", className="figure"),
                ], className="row-container"),
        ])

wave_1_tab2_figures = html.Div([
            html.Div([
                dcc.Graph(id="figure-1", className="figure"),
                dcc.Graph(id="figure-2", className="figure"),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="figure-3", className="figure"),
                dcc.Graph(id="figure-4", className="figure"),
                ], className="row-container"),
        ])

wave_1_tab3_figures = html.Div([
            html.Div([
                dcc.Graph(id="figure-1", className="figure"),
                dcc.Graph(id="figure-2", className="figure"),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="figure-3", className="figure"),
                dcc.Graph(id="figure-4", className="figure"),
                ], className="row-container"),
        ])


wave_1_figure_groups = {
    "wave-1-demographics-tab" : wave_1_demographic_figures,
    "tab-2" : wave_1_tab2_figures,
    "tab-3" : wave_1_tab3_figures,
}

wave_1_tabs = html.Div(
    [
        dbc.Tabs([
            dbc.Tab(label="Demographics", id="wave-1-demographics-tab", className="nav-item"),
            dbc.Tab(label="Tab 2", id="tab-2", className="nav-item"),
            dbc.Tab(label="Tab 3", id="tab-3", className="nav-item"),
        ],
            id="wave-1-tabs",
            active_tab="wave-1-demographics-tab",
            className="nav-fill justify-content-center",
        ),
        html.Div(id="content"),
    ]
)


app.layout = html.Div([
    html.Link(
        rel='stylesheet',
        href='/assets/custom.css'  # Path to your custom CSS file
        ),
    html.Script(
        src='/assets/script.js'  # Path to your JavaScript file
    ),  
    Navbar,
    html.Div([
        html.H1("Welcome to Your Dashboard", style={"text-align": "center", "color": text_color}),  # Use the hex color code for text color
    ]),
    filter_options,
    wave_1_tabs,
])


@app.callback(Output("content", "children"), [Input("wave-1-tabs", "active_tab")])
def update_wave_1_tab(selected_tab):
    print(selected_tab)
    if selected_tab == "tab-1":
        return wave_1_figure_groups["tab-2"]
    elif selected_tab == "tab-2":
        return wave_1_figure_groups["tab-3"]
    return wave_1_figure_groups["wave-1-demographics-tab"]

if __name__ == '__main__':
    app.run_server(debug=True)
