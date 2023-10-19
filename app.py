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

def update_filters_select_unselect_all(btn1,btn2,btn3,btn4,feature_options_gender,feature_options_language,feature_options_community,feature_options_income):
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


@app.callback(
    [Output('wave-2-age-histogram', 'figure'),
     Output('wave-2-lang-pie-chart', 'figure'),
     Output('wave-2-community-pie-chart', 'figure'),
     Output('wave-2-gender-bar-chart', 'figure'),],
    [Input('gender_filter', 'value'),
    Input('language_filter', 'value'),
    Input('community_filter', 'value'),
    Input('income_filter', 'value'),])
def callback_func(gender_values,language_values,community_values,income_values):
    
    temp_df = wave2_df[wave2_df["Gender"].isin(gender_values)]
    temp_df = temp_df[temp_df["Language"].isin(language_values)]
    temp_df = temp_df[temp_df["Community"].isin(community_values)]
    temp_df = temp_df[temp_df["Income"].isin(income_values)]
    wave_2_age_histogram = create_histogram(temp_df, 'Age', title_text="Age Distribution", num_bins=15)
    wave_2_lang_pie_chart = create_pie_chart(temp_df, 'Language', 'counter_column', 'Language')
    wave_2_community_pie_chart = create_pie_chart(temp_df, 'Community', 'counter_column', 'Community')
    wave_2_gender_bar_chart = create_horizontal_bar_chart(temp_df, 'Gender', 'Gender')
    pathname = [gender_values,language_values,community_values,income_values]
    return [wave_2_age_histogram,wave_2_lang_pie_chart,wave_2_community_pie_chart,wave_2_gender_bar_chart ]




if __name__ == '__main__':
    app.run_server(debug=True)


