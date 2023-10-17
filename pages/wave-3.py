import dash
from dash import html, dcc, callback, Input, Output

from components.wave_3_components import *

dash.register_page(__name__)

layout = html.Div([ 
    wave_3_title,
    wave_3_tabs,
])

@callback(Output("wave-3-content", "children"), [Input("wave-3-tabs", "active_tab")])
def update_wave_3_tab(selected_tab):
    print(selected_tab)
    if selected_tab == "tab-1":
        return wave_3_figure_groups["tab-2"]
    elif selected_tab == "tab-2":
        return wave_3_figure_groups["tab-3"]
    return wave_3_figure_groups["wave-3-demographics-tab"]