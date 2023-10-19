import dash
from dash import html, dcc, callback, Input, Output


from components.wave_2_components import *


dash.register_page(__name__)

layout = html.Div([ 
    wave_2_title,
    wave_2_tabs,


    # invisible block to register ids. need to find a workaround!!!!
    # html.Div(style = {'display':'none'},
    #                      children = [wave_2_figure_groups["wave-2-demographics-tab"]]),
    
])

@callback(Output("wave-2-content", "children"), [Input("wave-2-tabs", "active_tab")])
def update_wave_2_tab(selected_tab):
    print(selected_tab)
    if selected_tab == "tab-1":
        return wave_2_figure_groups["tab-2"]
    elif selected_tab == "tab-2":
        return wave_2_figure_groups["tab-3"]
    return wave_2_figure_groups["wave-2-demographics-tab"]



