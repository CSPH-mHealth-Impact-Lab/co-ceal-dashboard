import plotly.express as px
import plotly.graph_objects as go
import os
from dash import html, dcc
import numpy as np
import pandas as pd

graph_title_font_color = os.environ.get("graph_title_font_color", "#333")
graph_title_font_size = int(os.environ.get("graph_title_font_size", 18))

hover_bgcolor="white"
hover_font_size=16
hover_font_family="Rockwell"
hover_font_color="black"

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

# Function to create a histogram with updated layout
def create_histogram(data, column, title_text, num_bins=10, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    data_cleaned = data.dropna(subset=[column])
    fig = px.histogram(data_cleaned, x=column, nbins=num_bins, labels={column: 'Age'},text_auto=True)
    
    # Customize the appearance of the histogram
    fig.update_traces(marker_color='rgb(93, 92, 244)', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.9)
    
    # Customize the title, font, and layout settings directly
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        xaxis_title='Age',
        yaxis_title='Count',
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95  # Adjust the vertical position of the title
    )

    fig.update_layout(
        hoverlabel=dict(
        bgcolor=hover_bgcolor,
        font_size=hover_font_size,
        font_family=hover_font_family,
        font_color = hover_font_color
    )
)

    return fig

def create_histogram1(data, column, title_text, num_bins=10, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    data_cleaned = data.dropna(subset=[column])

    # Create a histogram using go.Histogram
    fig = go.Figure(go.Histogram(
        x=data_cleaned[column],
        nbinsx=num_bins,
        marker_color='rgb(93, 92, 244)',
        marker_line_color='rgb(8, 48, 107)',
        marker_line_width=1.5,
        opacity=0.9,
        texttemplate="%{y}", textfont_size=10,
        hoverinfo = ['x','y','name'],  # Make it a horizontal bar chart
        hovertemplate="Age: %{x}<br>Count: %{y}<extra></extra>",
    ))
    
    # Customize the title, font, and layout settings directly
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        xaxis_title='Age',
        yaxis_title='Count',
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95  # Adjust the vertical position of the title
    )

    return fig

# Function to create a pie chart with updated layout
def create_pie_chart(data, category_column, count_column, title_text, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    data_cleaned = data.dropna(subset=[category_column])

    # Create a pie chart
    fig = go.Figure(data=[go.Pie(
        labels=data_cleaned[category_column],
        values=data_cleaned[count_column],
        hovertemplate = "%{label} <br>Percentage: %{percent} <br> Count: %{value}"
    )])

    # Set the title and customize layout
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95  # Adjust the vertical position of the title
    )
    fig.update_layout(
        hoverlabel=dict(
        bgcolor=hover_bgcolor,
        font_size=hover_font_size,
        font_family=hover_font_family,
        font_color = hover_font_color
    )
)

    return fig

# Function to create a horizontal bar chart with updated layout

def create_horizontal_bar_chart(data, column, title_text, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    data_cleaned = data.dropna(subset=[column])

    # Group the data by the specified column and count occurrences
    counts = data_cleaned[column].value_counts().reset_index()
    counts.columns = [column, 'Count']

    # Sort the counts by the 'Count' column in descending order
    counts = counts.sort_values(by='Count', ascending=True)

    # Calculate the percentage for each value and round to 1 decimal point
    total_count = len(data_cleaned)
    counts['Percentage'] = (counts['Count'] / total_count) * 100
    counts['Percentage'] = counts['Percentage'].round(1)

    # Create a horizontal bar chart using go.Bar
    fig = go.Figure(go.Bar(
        x=counts['Count'],  # Use 'Count' as the x-value
        y=counts[column],
        text=[f'{count}<br>({percentage}%)' for count, percentage in zip(counts['Count'], counts['Percentage'])],
        orientation='h',  # Make it a horizontal bar chart
        hovertemplate=" %{label}<br>Count: %{x}<br><extra></extra> "
    ))

    # Customize the appearance of the chart
    fig.update_traces(marker_color='rgb(153, 102, 204)', marker_line_color='rgb(8, 48, 107)',
                      marker_line_width=1.5, opacity=0.9)

    # Customize the font and layout settings
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        xaxis_title='Count',  # Change x-axis label to 'Count'
        yaxis_title='',  # Hide y-axis label
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95,  # Adjust the vertical position of the title
        xaxis=dict(range=[0, counts['Count'].sum()])  # Set x-axis scale based on max count
    )
    fig.update_layout(
        hoverlabel=dict(
        bgcolor=hover_bgcolor,
        font_size=hover_font_size,
        font_family=hover_font_family,
        font_color = hover_font_color
    )
)
    fig.update_traces(texttemplate='%{text}', textposition='outside')

    return fig


def create_donut_chart(data, category_column, count_column, title_text, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    data_cleaned = data.dropna(subset=[category_column])

    # Create a pie chart
    fig = go.Figure(data=[go.Pie(
        labels=data_cleaned[category_column],
        values=data_cleaned[count_column],
        hole=.7,
        hovertemplate = "%{label} <br>Percentage: %{percent} <br> Count: %{value}",
                                 insidetextorientation='radial'
    )])

    # Set the title and customize layout
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95  # Adjust the vertical position of the title
    )
    fig.update_layout(
        hoverlabel=dict(
        bgcolor=hover_bgcolor,
        font_size=hover_font_size,
        font_family=hover_font_family,
        font_color = hover_font_color
    )
)

    return fig

#'label'+'text'+'value'+'current path'+'percent root'+'percent entry'+'percent parent'
def create_icicle_chart(data, label_column,parent_column, count_column, title_text, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    data_cleaned = data.dropna(subset=[label_column,parent_column])
    fig = px.treemap(data_cleaned, path=[px.Constant("Total"), parent_column,label_column], values=count_column, 
                hover_data=[count_column])
    # fig = px.icicle(data_cleaned, path=[px.Constant("Total"), parent_column,label_column], values=count_column, 
    #             hover_data=[count_column])
    fig.update_traces(root_color="cyan")
    fig.update_traces(texttemplate="%{label}<br>Count: %{value}")
    fig.data[0].textinfo = 'label + text + value + current path + percent root + percent entry + percent parent'

    fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95  # Adjust the vertical position of the title
    )
    return fig

def covid_testing_bar_chart(data,title_text, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    constant_value1 = 75.2
    constant_value2 = 35.2
    columns_list = ['ceal_testbehavior','ceal2_testpositive']
    columns_list_new = ['% tested for COVID','% tested positive for COVID']
    grouped_df = data.groupby('Community').agg(Count=('Community', 'count'), **{col: (col, lambda x: (x==1).sum()) for col in columns_list}).reset_index()
    for col in columns_list:
        grouped_df[col] = grouped_df[col] * 100 / grouped_df['Count']
        grouped_df[col] = grouped_df[col].round(1)

    rename_dict = dict(zip(columns_list, columns_list_new))
    grouped_df.rename(columns=rename_dict, inplace=True)
    fig = go.Figure(data=[
    go.Bar(name='% tested for COVID', y=grouped_df['Community'], x=grouped_df['% tested for COVID'], orientation='h', marker_color=px.colors.qualitative.Antique[4]),
    go.Bar(name='% tested positive for COVID', y=grouped_df['Community'], x=grouped_df['% tested positive for COVID'], orientation='h', marker_color=px.colors.qualitative.Light24[8])
])

    # Add vertical line for a constant value
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Antique[4]), y0=-0.5, y1=grouped_df.shape[0],
        x0=constant_value1, x1=constant_value1
    )
    # Add label to the line
    fig.add_annotation(
        y=grouped_df.shape[0], x=constant_value1+2,text="avg: 75.2",
        showarrow=False,font=dict(size=10,color="black"),)

    # Add another vertical line for another constant value
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Light24[8]), y0=0, y1=grouped_df.shape[0],
        x0=constant_value2, x1=constant_value2)
    fig.add_annotation(
        y=grouped_df.shape[0], x=constant_value2+2,text="avg: 35.2",
        showarrow=False,font=dict(size=10,color="black"),)

    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95,  # Adjust the vertical position of the title
        yaxis=dict(tickfont=dict(size=11)),
        xaxis=dict(title="percentage"),
        legend=dict(orientation="h",yanchor="bottom",y=1,xanchor="right",x=1)  # Decrease font size for x axis labels
    )
    return fig

def flu_vaccine_bar_chart(data,title_text, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    temp_flu_df = data.groupby('Community').agg(Count=('Community', 'count'), **{'flu_vax_season21_22': ('flu_vax_season21_22', lambda x: (x==1).sum())}).reset_index()
    col = 'flu_vax_season21_22'
    temp_flu_df[col] = temp_flu_df[col] * 100 / temp_flu_df['Count']
    temp_flu_df[col] = temp_flu_df[col].round(1)
    temp_flu_df.rename(columns={'flu_vax_season21_22': '% vaccinated for flu'}, inplace=True)
    temp_flu_df.drop(columns=['Count'], inplace=True)

    temp_ch_df = data[(data["parent_ch1217"]==1) | (data["parent_ch511"]==1) | (data["parent_ch04"]==1)]
    temp_ch_df = temp_ch_df.groupby('Community').agg(Count=('Community', 'count'), **{'flu_vax_season21_22_ch': ('flu_vax_season21_22_ch', lambda x: (x==1).sum())}).reset_index()
    col = 'flu_vax_season21_22_ch'
    temp_ch_df[col] = temp_ch_df[col] * 100 / temp_ch_df['Count']
    temp_ch_df[col] = temp_ch_df[col].round(1)
    temp_ch_df.rename(columns={'flu_vax_season21_22_ch': '% vaccinated children for flu'}, inplace=True)
    temp_ch_df.drop(columns=['Count'], inplace=True)

    flu_df = pd.merge(temp_ch_df, temp_flu_df, on='Community')
    constant_value1 = flu_df['% vaccinated for flu'].mean()
    constant_value2 = flu_df['% vaccinated children for flu'].mean()

    fig = go.Figure(data=[
    go.Bar(name='% vaccinated for flu', y=flu_df['Community'], x=flu_df['% vaccinated for flu'], orientation='h', marker_color=px.colors.qualitative.Antique[4]),
    go.Bar(name='% vaccinated children for flu', y=flu_df['Community'], x=flu_df['% vaccinated children for flu'], orientation='h', marker_color=px.colors.qualitative.Light24[8])
    ])
    fig.add_shape(type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Antique[4]), y0=-0.5, 
                  y1=flu_df.shape[0],x0=constant_value1, x1=constant_value1)
    # Add label to the line
    fig.add_annotation(y=flu_df.shape[0], x=constant_value1+2,text="avg: 58.8",
        showarrow=False,font=dict(size=10,color=px.colors.qualitative.Antique[4]),)

    # Add another vertical line for another constant value
    fig.add_shape(type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Light24[8]), 
                  y0=0, y1=flu_df.shape[0],x0=constant_value2, x1=constant_value2)
    fig.add_annotation(
        y=flu_df.shape[0], x=constant_value2-2,text="avg: 58.3",
        showarrow=False,font=dict(size=10,color=px.colors.qualitative.Light24[8]),)

    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.update_layout(
        title_text="Flu vaccine behaviour",
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95,  # Adjust the vertical position of the title
        yaxis=dict(tickfont=dict(size=11)),
        xaxis=dict(title="percentage"),
        legend=dict(orientation="h",yanchor="bottom",y=1,xanchor="right",x=1)  # Decrease font size for x axis labels
    )

    return fig

def trust_by_community(data,title_text):
    temp_df = data.copy()
    trust_cols = [col for col in temp_df.columns if 'trust_ceal' in col and 'trial' not in col]
    temp_df[trust_cols] = temp_df[trust_cols].replace(98, None)
    temp_df[trust_cols] = temp_df[trust_cols].replace(990, None)
    temp_df = temp_df.groupby('Community')[trust_cols].mean().reset_index()
    temp_df['trust_avg'] = temp_df[trust_cols].mean(axis=1)
    temp_df_melted = pd.melt(temp_df, id_vars=["Community"], var_name="variable", value_name="value")
    graph_df = temp_df_melted[temp_df_melted['variable']=='trust_avg']
    fig = go.Figure(data=[go.Bar(name='Trust by Community', y=graph_df['Community'], x=graph_df['value'], marker_color=px.colors.qualitative.Antique[4],orientation='h'),])
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95,  # Adjust the vertical position of the title
        yaxis=dict(tickfont=dict(size=11)),
        legend=dict(orientation="h",yanchor="bottom",y=1,xanchor="right",x=1),  # Decrease font size for x axis labels
        xaxis=dict(
        range=[0, 2],  # Set x axis range as 0-3
        tickvals=[0, 1, 2],
        ticktext=["Not at all", "A little", "A great deal"]
    )
    )
    return fig

def trust_by_category(data,title_text):
    temp_df = data.copy()
    trust_cols = [col for col in temp_df.columns if 'trust_ceal' in col and 'trial' not in col]
    temp_df[trust_cols] = temp_df[trust_cols].replace(98, None)
    temp_df[trust_cols] = temp_df[trust_cols].replace(990, None)
    temp_df = temp_df.groupby('Community')[trust_cols].mean().reset_index()
    temp_df['trust_avg'] = temp_df[trust_cols].mean(axis=1)
    temp_df_melted = pd.melt(temp_df, id_vars=["Community"], var_name="variable", value_name="value")
    fig = go.Figure(data=[go.Bar(name='Trust by Community', y=temp_df_melted['variable'], x=temp_df_melted['value'], marker_color=px.colors.qualitative.Antique[4],orientation='h'),])
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95,  # Adjust the vertical position of the title
        yaxis=dict(tickfont=dict(size=11),
                   tickvals=['trust_avg','trust_ceal2_commorg','trust_ceal2_tribal','trust_ceal_socialmed_r2','trust_ceal_faith_r2',
                    'trust_ceal_dr_r2','trust_ceal2_cdc','trust_ceal2_stgov','trust_ceal2_fedgov','trust_ceal_news','trust_ceal_coworkers','trust_ceal_friendsfam'],
                    ticktext=['Average Trust','Community Organization','Tribal leadership','Social Media','Faith Leader',
                    'Doctor or health care provider','CDC','State and/or local government','The federal government','News','People you go to work or class with','Your close friends and family']),
        legend=dict(orientation="h",yanchor="bottom",y=1,xanchor="right",x=1),  # Decrease font size for x axis labels
        xaxis=dict(
        range=[0, 2],  # Set x axis range as 0-3
        tickvals=[0, 1, 2],
        ticktext=["Not at all", "A little", "A great deal"]
    )
    )
    return fig

def covid_vaccine_bar_chart(data,title_text, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    constant_value1 = 81.8
    constant_value2 = 47.3
    columns_list = ['ceal2_covid_vaxdose','covid_boost']
    columns_list_new = ['Atleast one dose','Received booster dose']
    grouped_df = data.groupby('Community').agg(Count=('Community', 'count'), **{col: (col, lambda x: ((x==1) | (x==2) | (x==3)).sum()) for col in columns_list}).reset_index()
    for col in columns_list:
        grouped_df[col] = grouped_df[col] * 100 / grouped_df['Count']
        grouped_df[col] = grouped_df[col].round(1)

    rename_dict = dict(zip(columns_list, columns_list_new))
    grouped_df.rename(columns=rename_dict, inplace=True)
    fig = go.Figure(data=[
    go.Bar(name='Atleast one dose', y=grouped_df['Community'], x=grouped_df['Atleast one dose'], orientation='h', marker_color=px.colors.qualitative.Antique[4]),
    go.Bar(name='Received booster dose', y=grouped_df['Community'], x=grouped_df['Received booster dose'], orientation='h', marker_color=px.colors.qualitative.Light24[8])
])

    # Add vertical line for a constant value
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Antique[4]), y0=-0.5, y1=grouped_df.shape[0],
        x0=constant_value1, x1=constant_value1
    )
    # Add label to the line
    fig.add_annotation(
        y=grouped_df.shape[0], x=constant_value1+2,text="avg: 81.8",
        showarrow=False,font=dict(size=10,color="black"),)

    # Add another vertical line for another constant value
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Light24[8]), y0=0, y1=grouped_df.shape[0],
        x0=constant_value2, x1=constant_value2)
    fig.add_annotation(
        y=grouped_df.shape[0], x=constant_value2+2,text="avg: 47.3",
        showarrow=False,font=dict(size=10,color="black"),)

    # Change the bar mode
    fig.update_layout(barmode='group')
    fig.update_layout(
        title_text=title_text,
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95,  # Adjust the vertical position of the title
        yaxis=dict(tickfont=dict(size=11)),
        xaxis=dict(title="percentage"),
        legend=dict(orientation="h",yanchor="bottom",y=1,xanchor="right",x=1)  # Decrease font size for x axis labels
    )
    return fig