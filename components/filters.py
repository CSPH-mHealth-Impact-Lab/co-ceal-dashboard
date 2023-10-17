import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

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

show_hide_button = html.Button("Hide Filters", id="show-hide-button", className="btn btn-danger m-2")

filter_container = html.Div([
        
        filter_options,
    ], id="filter-container", style={"display": "block"})

@callback(
    [Output("filter-container", "style"), Output("show-hide-button", "children"), Output("show-hide-button", "className")],
    Input("show-hide-button", "n_clicks"),
    prevent_initial_call=True
)
def toggle_filter_visibility(n_clicks):
    if n_clicks is None:
        n_clicks = 0

    if n_clicks % 2 == 0:  # Toggle the visibility on even clicks
        return {"display": "block"}, "Hide Filters", "btn btn-danger m-2"
    else:
        return {"display": "none"}, "Show Filters", "btn btn-primary m-2"
    