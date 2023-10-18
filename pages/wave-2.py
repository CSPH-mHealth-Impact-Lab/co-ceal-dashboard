import dash
from dash import html, dcc, callback, Input, Output


from components.wave_2_components import *



dash.register_page(__name__)

layout = html.Div([ 
    wave_2_title,
    wave_2_tabs,
])

@callback(Output("wave-2-content", "children"), [Input("wave-2-tabs", "active_tab")])
def update_wave_2_tab(selected_tab):
    print(selected_tab)
    if selected_tab == "tab-1":
        return wave_2_figure_groups["tab-2"]
    elif selected_tab == "tab-2":
        return wave_2_figure_groups["tab-3"]
    return wave_2_figure_groups["wave-2-demographics-tab"]

def apply_filter_for_figure(data, selected_data, column_name):
    if selected_data is None:
        return data  # No filter applied, return the original data

    # Extract the selected data range
    x_range = selected_data["x"]
    
    if x_range is not None and len(x_range) == 2:
        min_value, max_value = x_range
        
        # Apply the filter based on the selected range
        filtered_data = data[(data[column_name] >= min_value) & (data[column_name] <= max_value)]
        return filtered_data

    return data

