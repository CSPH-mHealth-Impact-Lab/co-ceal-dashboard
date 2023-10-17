import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output


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