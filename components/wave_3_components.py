import dash_bootstrap_components as dbc
from dash import html, dcc, callback, Input, Output,dash_table
import dash
import pandas as pd
from custom_functions.custom_functions import *
import os
from dotenv import load_dotenv
import plotly.express as px
load_dotenv()


wave3_df = pd.read_excel("data/wave_3.xlsx",engine='openpyxl')
wave3_df['Gender_recoded'] = wave3_df['Gender'].apply(lambda x: x if x in ['Man', 'Woman'] else 'Other Gender')
print("number of rows in wave 3 data: ", wave3_df.shape[0]) 

displayModeBar_str = os.environ.get("displayModeBar", "True")
displayModeBar = displayModeBar_str.lower() == "true"
displaylogo_str = os.environ.get("displaylogo", "True")
displaylogo = displaylogo_str.lower() == "true"


wave_3_title = html.Div([
    html.H1("Welcome to Your Dashboard for Wave 3", className="my-custom-title text-center"),
])

wave_3_age_histogram = create_histogram(wave3_df, 'Age', title_text="Age Distribution", num_bins=15)
wave_3_lang_pie_chart = create_pie_chart(wave3_df, 'Language', 'counter_column', 'Survey Language Distribution')
wave_3_community_icicle_chart = create_icicle_chart(wave3_df,'Are you Hispanic or Latino? ','Community', 'counter_column', "Community Ethnicity Chart")
wave_3_gender_bar_chart = create_horizontal_bar_chart(wave3_df, 'Gender', 'Gender')

wave_3_testing_bar_chart = covid_testing_bar_chart(wave3_df, 'COVID Testing Behaviour')
wave_3_flu_vacaine_bar_chart = flu_vaccine_bar_chart(wave3_df, 'Flu Vaccine Behaviour')
wave_3_trust_by_community_bar_chart = trust_by_community(wave3_df, 'Average Trust by Community')
wave_3_vaccine_bar_chart = covid_vaccine_bar_chart(wave3_df, 'COVID Vaccination Behaviour')

vax_reasons_bar = create_vax_reasons_bar(wave3_df, 'Reason','Reasons for Getting Vaccine',replace_dict_vax_reasons_w3, replace_dict_vax_reasons_children_w3)
vax_concerns_bar = create_vax_challenges_bar(wave3_df, 'Challenges','Challenges for getting vaccine',replace_dict_vax_challngs_w3, replace_dict_vax_challngs_children_w3)
vax_barriers_bar = create_vax_barriers_bar(wave3_df, 'Barriers','Barriers for getting vaccine',replace_dict_vax_barriers_adults_w3, replace_dict_vax_barriers_children_w3)
vax_concerns_got_bar = create_vax_concerns_got_bar(wave3_df, 'Concerns','Concerns for people who got vaccine',replace_dict_vax_concerns_adults_w3, replace_dict_vax_concerns_children_w3)


wave_3_demographic_figures = html.Div([
            html.Div([
                dcc.Graph(id="wave-3-age-histogram", className="figure",figure=wave_3_age_histogram,
                          config={"displayModeBar": True, "displaylogo": displayModeBar},),
                dcc.Graph(id="wave-3-lang-pie-chart", className="figure",figure=wave_3_lang_pie_chart,
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="wave-3-community-icicle-chart", className="figure", figure = wave_3_community_icicle_chart,
                          config={"displayModeBar": True, "displaylogo": displayModeBar},),
                dcc.Graph(id="wave-3-gender-bar-chart", className="figure", figure = wave_3_gender_bar_chart,
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},),
                ], className="row-container"),
        ])


wave_3_tab2_figures = html.Div([
            html.Div([
                dcc.Graph(id="wave-3-testing-bar-chart", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=wave_3_testing_bar_chart,),
                dcc.Graph(id="wave-3-trust-by-community-bar-chart", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=wave_3_trust_by_community_bar_chart),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="wave-3-flu-vaccine-bar-chart", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=wave_3_flu_vacaine_bar_chart),
                dcc.Graph(id="wave-3-vaccine-bar-chart", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=wave_3_vaccine_bar_chart),
                ], className="row-container"),
        ])

wave_3_tab3_figures = html.Div([
            html.Div([
                dcc.Graph(id="wave-3-vaccine-reasons", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=vax_reasons_bar,),
                dcc.Graph(id="wave-3-vaccine-challenges", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=vax_concerns_bar),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="wave-3-vaccine-barriers", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=vax_barriers_bar),
                dcc.Graph(id="wave-3-vaccine-concerns-got", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=vax_concerns_got_bar),
                ], className="row-container"),
        ])


wave_3_figure_groups = {
    "wave-3-demographics-tab" : wave_3_demographic_figures,
    "tab-2" : wave_3_tab2_figures,
    "tab-3" : wave_3_tab3_figures,
}

wave_3_tabs = html.Div(
    [
        dbc.Tabs([
            dbc.Tab(label="Demographics", id="wave-3-demographics-tab", className="nav-item",
                    active_tab_style={"textTransform": "uppercase"}, active_label_style={"color": "#FB79B3"}, 
                    active_tab_class_name="fw-bold fst-italic", activeLabelClassName="text-success"),
            dbc.Tab(label="Vaccine Behaviour", id="tab-2", className="nav-item",
                    active_tab_style={"textTransform": "uppercase"}, active_label_style={"color": "#FB79B3"}, 
                    active_tab_class_name="fw-bold fst-italic", activeLabelClassName="text-success"),
            dbc.Tab(label="Reasons, Challenges, Concerns & Barriers", id="tab-3", className="nav-item",
                    active_tab_style={"textTransform": "uppercase"}, active_label_style={"color": "#FB79B3"}, 
                    active_tab_class_name="fw-bold fst-italic", activeLabelClassName="text-success"),
        ],
            id="wave-3-tabs",
            active_tab="wave-3-demographics-tab",
            className="nav-fill justify-content-center",
        ),
        html.Div(id="wave-3-content"),
    ]
)