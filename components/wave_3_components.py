import dash_bootstrap_components as dbc
from dash import html, dcc

from dotenv import load_dotenv
import os

load_dotenv()

displayModeBar_str = os.environ.get("displayModeBar", "True")
displayModeBar = displayModeBar_str.lower() == "true"
displaylogo_str = os.environ.get("displaylogo", "True")
displaylogo = displaylogo_str.lower() == "true"

graph_title_font_color = os.environ.get("graph_title_font_color", "#333")
graph_title_font_size = int(os.environ.get("graph_title_font_size", 18))


wave_3_title = html.Div([
    html.H1("Welcome to Your Dashboard for Wave 3", className="my-custom-title text-center"),
])


def get_figure_layout(title, font_color=graph_title_font_color, font_size=graph_title_font_size):
    return {
        "layout": {
            "title": {
                "text": title,
                "font": {
                    "size": font_size,  # Customize font size as needed
                    "color": font_color,  # Customize font color (default is #333)
                },
            },
        },
    }

wave_3_demographic_figures = html.Div([
            html.Div([
                dcc.Graph(id="figure-1", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 1 fig 1"),),
                dcc.Graph(id="figure-2", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 1 fig 2"),),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="figure-3", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 1 fig 3"),),
                dcc.Graph(id="figure-4", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 1 fig 4"),),
                ], className="row-container"),
        ])

wave_3_tab2_figures = html.Div([
            html.Div([
                dcc.Graph(id="figure-1", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 2 fig 1"),),
                dcc.Graph(id="figure-2", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 2 fig 2"),),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="figure-3", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 2 fig 3"),),
                dcc.Graph(id="figure-4", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 2 fig 4"),),
                ], className="row-container"),
        ])

wave_3_tab3_figures = html.Div([
            html.Div([
                dcc.Graph(id="figure-1", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 3 fig 1"),),
                dcc.Graph(id="figure-2", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 3 fig 2"),),
                ], className="row-container"),
            html.Div([
                dcc.Graph(id="figure-3", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 3 fig 3"),),
                dcc.Graph(id="figure-4", className="figure",
                          config={"displayModeBar": displayModeBar, "displaylogo": displayModeBar},
                        figure=get_figure_layout("wave 3 tab 3 fig 4"),),
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
            dbc.Tab(label="Demographics", id="wave-3-demographics-tab", className="nav-item"),
            dbc.Tab(label="Tab 2", id="tab-2", className="nav-item"),
            dbc.Tab(label="Tab 3", id="tab-3", className="nav-item"),
        ],
            id="wave-3-tabs",
            active_tab="wave-3-demographics-tab",
            className="nav-fill justify-content-center",
        ),
        html.Div(id="wave-3-content"),
    ]
)