import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output

available_languages = ['English', 'Somali', 'Spanish']
available_genders = ['Man', 'Woman', 'Transgender female or trans woman', 'Other',
       'Prefer not to answer', 'Transgender male or trans man',
       'Nonbinary, genderqueer, or gender fluid']
available_communities = ['PUEBLO Urban Latina/o/x', 'DENVER Urban AA/Black',
       'SLV Rural Latina/o/x', 'FT MORGAN/GREELEY Rural AA/Black',
       'DENVER Urban Latina/o/x',
       'DENVER Urban American Indian/Alaska Native']

available_incomes = ['Less than $15,000', '$20,000-$24,999', '$25,000-$34,999',
       '$35,000-$49,999', '$15,000-$19,999', '$50,000-$74,999',
       'Prefer not to answer', '$100,000 and above',
       '$75,000-$99,999']

filter_options = html.Div([

    html.Div([
        dbc.DropdownMenu(
            children=[
                html.Button('Select/Unselect all', id='select_all_genders', className="btn btn-success m-3 p-3"),
                dbc.Checklist(
                    id='gender_filter',
                    options=[{"value": i, "label": ' ' + i} for i in available_genders],
                    value=available_genders,
                    inline=True,
                    className="m-1 p-1",
                )
            ],
            label="Gender",
            className="text-center",  # Center the dropdown menu button horizontally
            toggleClassName="d-flex flex-column align-items-center justify-content-center w-100"
        ),
    ], className="filter m-3 justify-content-center"),

    html.Div([
        dbc.DropdownMenu(
            children=[
                html.Button('Select/Unselect all', id='select_all_languages', className="btn btn-success m-1 p-1"),
                dbc.Checklist(
                    id='language_filter',
                    options=[{"value": i, "label": ' ' + i} for i in available_languages],
                    value=available_languages,
                    inline=True,
                    className="m-1 p-1",
                )
            ],
            label="Language",
            className="text-center",  # Center the dropdown menu button horizontally
            toggleClassName="d-flex flex-column align-items-center justify-content-center w-100"
        ),
    ], className="filter m-3"),

    html.Div([
        dbc.DropdownMenu(
            children=[
                html.Button('Select/Unselect all', id='select_all_community', className="btn btn-success m-1 p-1"),
                dbc.Checklist(
                    id='community_filter',
                    options=[{"value": i, "label": ' ' + i} for i in available_communities],
                    value=available_communities,
                    inline=True,
                    className="m-1 p-1",
                )
            ],
            label="Community",
            className="text-center",  # Center the dropdown menu button horizontally
            toggleClassName="d-flex flex-column align-items-center justify-content-center w-100"
        ),
    ], className="filter m-3"),

    html.Div([
        dbc.DropdownMenu(
            children=[
                html.Button('Select/Unselect all', id='select_all_income', className="btn btn-success m-1 p-1"),
                dbc.Checklist(
                    id='income_filter',
                    options=[{"value": i, "label": ' ' + i} for i in available_incomes],
                    value=available_incomes,
                    inline=True,
                    className="m-1 p-1",
                )
            ],
            label="Income",
            className="text-center",  # Center the dropdown menu button horizontally
            toggleClassName="d-flex flex-column align-items-center justify-content-center w-100"
        ),
    ], className="filter m-3"),
], className="filter-container")


show_hide_button = html.Button("Show Filters", id="show-hide-button", className="btn btn-primary m-2")

filter_container = html.Div([
        
        filter_options,
    ], id="filter-container", style={"display": "none"})

@callback(
    [Output("filter-container", "style"), Output("show-hide-button", "children"), Output("show-hide-button", "className")],
    Input("show-hide-button", "n_clicks"),
    prevent_initial_call=True
)
def toggle_filter_visibility(n_clicks):
    if n_clicks is None:
        n_clicks = 0

    if n_clicks % 2 != 0:  # Toggle the visibility on even clicks
        # return {"display": "none"}, "Show Filters", "btn btn-primary m-2"
        return {"display": "block"}, "Hide Filters", "btn btn-danger m-2"  
    else:
        # return {"display": "block"}, "Hide Filters", "btn btn-danger m-2"
        return {"display": "none"}, "Show Filters", "btn btn-primary m-2"
    