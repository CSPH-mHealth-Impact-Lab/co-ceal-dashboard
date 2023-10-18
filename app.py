import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback_context, Input, Output, State
# from dash.dependencies import Input, Output, State

from components.navbar import *
from components.filters import *

from dotenv import load_dotenv
import os

load_dotenv()

filter_options = filter_options

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


@app.callback(
[Output('gender_filter', 'value'),
 Output('language_filter', 'value'),
 Output('community_filter', 'value'),
 Output('income_filter', 'value'),],
[Input('select_all_genders', 'n_clicks'),
 Input('select_all_languages', 'n_clicks'),
 Input('select_all_community', 'n_clicks'),
 Input('select_all_income', 'n_clicks'),],
[State('gender_filter', 'options'),
 State('language_filter', 'options'),
 State('community_filter', 'options'),
 State('income_filter', 'options'),])

def update_dropdown(btn1,btn2,btn3,btn4,feature_options_gender,feature_options_language,feature_options_community,feature_options_income):
    ctx = callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    print(input_id)
    gender_select_all = [i['value'] for i in feature_options_gender]
    language_select_all = [i['value'] for i in feature_options_language]
    community_select_all = [i['value'] for i in feature_options_community]
    income_select_all = [i['value'] for i in feature_options_income]
    if input_id == 'select_all_genders':

        if btn1 % 2 != 0: ## Clear all options on even clicks
            gender_select_all = []
            #return []
        else: ## Select all options on odd clicks
            gender_select_all = [i['value'] for i in feature_options_gender]
    elif input_id == 'select_all_languages':

        if btn2 % 2 != 0: ## Clear all options on even clicks
            language_select_all = []
            #return []
        else: ## Select all options on odd clicks
            language_select_all = [i['value'] for i in feature_options_language]
    elif input_id == 'select_all_community':

        if btn3 % 2 != 0: ## Clear all options on even clicks
            community_select_all = []
            #return []
        else: ## Select all options on odd clicks
            community_select_all = [i['value'] for i in feature_options_community]
    elif input_id == 'select_all_income':

        if btn4 % 2 != 0: ## Clear all options on even clicks
            income_select_all = []
            #return []
        else: ## Select all options on odd clicks
            income_select_all = [i['value'] for i in feature_options_income]

    return [gender_select_all,language_select_all,community_select_all,income_select_all]




if __name__ == '__main__':
    app.run_server(debug=True)


