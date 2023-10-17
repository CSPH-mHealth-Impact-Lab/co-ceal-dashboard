import dash_bootstrap_components as dbc
from dash import html, dcc

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
