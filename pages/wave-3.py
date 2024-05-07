import dash
from dash import html, dcc, callback, Input, Output

from components.wave_3_components import *

dash.register_page(__name__, path='/wave-3')

layout = html.Div([ 
    wave_3_title,
    wave_3_tabs,
])

@callback(Output("wave-3-content", "children"), [Input("wave-3-tabs", "active_tab")])
def update_wave_3_tab(selected_tab):
    print(selected_tab)
    if selected_tab == "tab-2":
        return wave_3_figure_groups["tab-3"]
    elif selected_tab == "tab-1":
        return wave_3_figure_groups["tab-2"]
    return wave_3_figure_groups["wave-3-demographics-tab"]

@callback(
    [Output('wave-3-age-histogram', 'figure'),
     Output('wave-3-lang-pie-chart', 'figure'),
     Output('wave-3-community-icicle-chart', 'figure'),
     Output('wave-3-gender-bar-chart', 'figure'),],
    [Input('gender_filter', 'value'),
    Input('language_filter', 'value'),
    Input('community_filter', 'value'),
    Input('income_filter', 'value'),])
def callback_func(gender_values,language_values,community_values,income_values):
    
    temp_df = wave3_df[wave3_df["Gender"].isin(gender_values)]
    temp_df = temp_df[temp_df["Language"].isin(language_values)]
    temp_df = temp_df[temp_df["Community"].isin(community_values)]
    temp_df = temp_df[temp_df["Income"].isin(income_values)]
    wave_3_age_histogram = create_histogram(temp_df, 'Age', title_text="Age Distribution", num_bins=15)
    wave_3_lang_pie_chart = create_pie_chart(temp_df, 'Language', 'counter_column', 'Survey Language Distribution')
    wave_3_community_pie_chart = create_icicle_chart(temp_df,'Are you Hispanic or Latino? ','Community', 'counter_column', "Community Ethnicity Chart")
    wave_3_gender_bar_chart = create_horizontal_bar_chart(temp_df, 'Gender', 'Gender')
    
    pathname = [gender_values,language_values,community_values,income_values]
    return [wave_3_age_histogram,wave_3_lang_pie_chart,wave_3_community_pie_chart,wave_3_gender_bar_chart ]


@callback(
    [Output('wave-3-testing-bar-chart', 'figure'),
     Output('wave-3-flu-vaccine-bar-chart', 'figure'),
     Output('wave-3-trust-by-community-bar-chart', 'figure'),
     Output('wave-3-vaccine-bar-chart', 'figure'),],
    [Input('gender_filter', 'value'),
    Input('language_filter', 'value'),
    Input('community_filter', 'value'),
    Input('income_filter', 'value'),])
def callback_func(gender_values,language_values,community_values,income_values):
    
    temp_df = wave3_df[wave3_df["Gender"].isin(gender_values)]
    temp_df = temp_df[temp_df["Language"].isin(language_values)]
    temp_df = temp_df[temp_df["Community"].isin(community_values)]
    temp_df = temp_df[temp_df["Income"].isin(income_values)]
    wave_3_testing_bar_chart = covid_testing_bar_chart(temp_df, 'COVID Testing Behaviour')
    wave_3_flu_vacaine_bar_chart = flu_vaccine_bar_chart(temp_df, 'Flu Vaccine Behaviour')
    wave_3_trust_by_community_bar_chart = trust_by_community(temp_df, "Average Trust by Community")
    wave_3_vaccine_bar_chart = covid_vaccine_bar_chart(temp_df, 'COVID Vaccination Behaviour')
    pathname = [gender_values,language_values,community_values,income_values]
    return [wave_3_testing_bar_chart,wave_3_flu_vacaine_bar_chart,wave_3_trust_by_community_bar_chart,wave_3_vaccine_bar_chart]


@callback(
    [Output('wave-3-vaccine-reasons', 'figure'),
     Output('wave-3-vaccine-challenges', 'figure'),
     Output('wave-3-vaccine-barriers', 'figure'),
     Output('wave-3-vaccine-concerns-got', 'figure'),],
    [Input('gender_filter', 'value'),
    Input('language_filter', 'value'),
    Input('community_filter', 'value'),
    Input('income_filter', 'value'),])
def callback_func(gender_values,language_values,community_values,income_values):
    
    temp_df = wave3_df[wave3_df["Gender"].isin(gender_values)]
    temp_df = temp_df[temp_df["Language"].isin(language_values)]
    temp_df = temp_df[temp_df["Community"].isin(community_values)]
    temp_df = temp_df[temp_df["Income"].isin(income_values)]
    vax_reasons_bar = create_vax_reasons_bar(temp_df, 'Reason','Reasons for Getting Vaccine',replace_dict_vax_reasons_w3, replace_dict_vax_reasons_children_w3)
    vax_concerns_bar = create_vax_challenges_bar(temp_df, 'Challenges','Challenges for getting vaccine',replace_dict_vax_challngs_w3, replace_dict_vax_challngs_children_w3)
    vax_barriers_bar = create_vax_barriers_bar(temp_df, 'Barriers','Barriers for getting vaccine',replace_dict_vax_barriers_adults_w3, replace_dict_vax_barriers_children_w3)
    vax_concerns_got_bar = create_vax_concerns_got_bar(temp_df, 'Concerns','Concerns for people who got vaccine',replace_dict_vax_concerns_adults_w3, replace_dict_vax_concerns_children_w3)

    pathname = [gender_values,language_values,community_values,income_values]
    return [vax_reasons_bar,vax_concerns_bar,vax_barriers_bar,vax_concerns_got_bar]

@callback(
    [Output('wave-3-trust-by-community-bar-chart', 'figure',allow_duplicate=True),],

    [Input('wave-3-trust-by-community-bar-chart', 'clickData'),],
    prevent_initial_call=True
)

def drilldown(click_data):
    ctx = dash.callback_context
    trigger_id = ctx.triggered[0]["prop_id"].split(".")[0]
    print(trigger_id)
    if trigger_id == 'wave-3-trust-by-community-bar-chart':
        
        if click_data is not None:
            click_data = click_data['points'][0]['label']
            print(click_data)
            if click_data not in wave3_df['Community'].unique():
                fig = trust_by_community(wave3_df, "Average Trust by Community")
                return [fig]
            temp_df = wave3_df[wave3_df["Community"]==click_data]
            fig = trust_by_category(temp_df,"Average Trust for "+click_data)
            return [fig]
    else:
        fig = trust_by_community(wave3_df, "Average Trust by Community")
    return [fig]