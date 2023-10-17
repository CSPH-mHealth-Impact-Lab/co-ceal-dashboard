import dash
from dash import html, dcc, callback, Input, Output

from components.wave_1_components import *

dash.register_page(__name__, path='/')

layout = html.Div([ 
    wave_1_title,
    wave_1_tabs,
])

@callback(Output("wave-1-content", "children"), [Input("wave-1-tabs", "active_tab")])
def update_wave_1_tab(selected_tab):
    print(selected_tab)
    if selected_tab == "tab-1":
        return wave_1_figure_groups["tab-2"]
    elif selected_tab == "tab-2":
        return wave_1_figure_groups["tab-3"]
    return wave_1_figure_groups["wave-1-demographics-tab"]