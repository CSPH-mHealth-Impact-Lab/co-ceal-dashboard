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
    print("number of rows in wave 2 data before drop: ", data.shape[0])
    data_cleaned = data.dropna(subset=[column])
    print("number of rows in wave 2 data after drop: ", data.shape[0])
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
def create_icicle_chart(data, label_column, parent_column, count_column, title_text, graph_title_font_color='black', graph_title_font_size=12):
    data_cleaned = data.dropna(subset=[label_column, parent_column])
    fig = px.treemap(data_cleaned, path=[px.Constant("Total"), parent_column, label_column], values=count_column)

    # Update traces to remove hover data
    fig.update_traces(root_color="cyan", hovertemplate=None)
    fig.update_traces(texttemplate="%{label}<br>Count: %{value}")

    # Update layout
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
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
    go.Bar(name='% tested for COVID', y=grouped_df['Community'], x=grouped_df['% tested for COVID'], orientation='h', 
           marker_color=px.colors.qualitative.Antique[4], hovertemplate='%{x}<extra></extra>'),
    go.Bar(name='% tested positive for COVID', y=grouped_df['Community'], x=grouped_df['% tested positive for COVID'], orientation='h',
            marker_color=px.colors.qualitative.Light24[8], hovertemplate='%{x}<extra></extra>')
])

    n = grouped_df['Community'].nunique()
    fig.add_trace(go.Scatter(
        x=[constant_value1]*n,
        y=[grouped_df['Community'][i] for i in range(n)],  # Span the entire y-axis
        mode='lines',
        line=dict(width=0.5, color='rgba(0,0,0,0)'),  # Thin and transparent line
        hoverinfo='text',
        hovertext=['avg: '+str(round(constant_value1,1))]*n,
        hoverlabel=dict(font_color='white',bgcolor=px.colors.qualitative.Antique[4]),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=[constant_value2]*n,
        y=[grouped_df['Community'][i] for i in range(n)],  # Span the entire y-axis
        mode='lines',
        line=dict(width=0.5, color='rgba(0,0,0,0)'),  # Thin and transparent line
        hoverinfo='text',
        hovertext=['avg: '+str(round(constant_value2,1))]*n,
        hoverlabel=dict(font_color='white',bgcolor=px.colors.qualitative.Light24[8]),
        showlegend=False
    ))

    # Add vertical line for a constant value
    max_y_coordinate = len(grouped_df['Community'].unique()) - 0.5  # Adjust based on your bar placement

    # Add vertical lines for constant values
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Antique[4]), 
        y0=0, y1=max_y_coordinate,
        x0=constant_value1, x1=constant_value1
    )
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Light24[8]), 
        y0=0, y1=max_y_coordinate,
        x0=constant_value2, x1=constant_value2
)

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
    go.Bar(name='% vaccinated for flu', y=flu_df['Community'], x=flu_df['% vaccinated for flu'], orientation='h', 
           marker_color=px.colors.qualitative.Antique[4], hovertemplate='%{x}<extra></extra>'),
    go.Bar(name='% vaccinated children for flu', y=flu_df['Community'], x=flu_df['% vaccinated children for flu'], orientation='h', 
           marker_color=px.colors.qualitative.Light24[8], hovertemplate='%{x}<extra></extra>')
    ])
    n = temp_ch_df['Community'].nunique()
    fig.add_trace(go.Scatter(
        x=[constant_value1]*n,
        y=[temp_ch_df['Community'][i] for i in range(n)],  # Span the entire y-axis
        mode='lines',
        line=dict(width=0.5, color='rgba(0,0,0,0)'),  # Thin and transparent line
        hoverinfo='text',
        hovertext=['avg: '+str(round(constant_value1,1))]*n,
        hoverlabel=dict(font_color='white',bgcolor=px.colors.qualitative.Antique[4]),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=[constant_value2]*n,
        y=[temp_ch_df['Community'][i] for i in range(n)],  # Span the entire y-axis
        mode='lines',
        line=dict(width=0.5, color='rgba(0,0,0,0)'),  # Thin and transparent line
        hoverinfo='text',
        hovertext=['avg: '+str(round(constant_value2,1))]*n,
        hoverlabel=dict(font_color='white',bgcolor=px.colors.qualitative.Light24[8]),
        showlegend=False
    ))
    max_y_coordinate = len(temp_ch_df['Community'].unique()) - 0.5  # Adjust based on your bar placement

    # Add vertical lines for constant values
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Antique[4]), 
        y0=0, y1=max_y_coordinate,
        x0=constant_value1, x1=constant_value1
    )
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Light24[8]), 
        y0=0, y1=max_y_coordinate,
        x0=constant_value2, x1=constant_value2
    )

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
    fig = go.Figure(data=[go.Bar(name='Trust by Community', y=graph_df['Community'], x=graph_df['value'],
                                  marker_color=px.colors.qualitative.Antique[4],orientation='h', hovertemplate='%{x}<extra></extra>'),])
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
    go.Bar(name='Atleast one dose', y=grouped_df['Community'], x=grouped_df['Atleast one dose'], orientation='h', 
           marker_color=px.colors.qualitative.Antique[4], hovertemplate='%{x}<extra></extra>'),
    go.Bar(name='Received booster dose', y=grouped_df['Community'], x=grouped_df['Received booster dose'], orientation='h',
            marker_color=px.colors.qualitative.Light24[8], hovertemplate='%{x}<extra></extra>')
])
    n = grouped_df['Community'].nunique()
    fig.add_trace(go.Scatter(
        x=[constant_value1]*n,
        y=[grouped_df['Community'][i] for i in range(n)],  # Span the entire y-axis
        mode='lines',
        line=dict(width=0.5, color='rgba(0,0,0,0)'),  # Thin and transparent line
        hoverinfo='text',
        hovertext=['avg: '+str(round(constant_value1,1))]*n,
        hoverlabel=dict(font_color='white',bgcolor=px.colors.qualitative.Antique[4]),
        showlegend=False
    ))
    fig.add_trace(go.Scatter(
        x=[constant_value2]*n,
        y=[grouped_df['Community'][i] for i in range(n)],  # Span the entire y-axis
        mode='lines',
        line=dict(width=0.5, color='rgba(0,0,0,0)'),  # Thin and transparent line
        hoverinfo='text',
        hovertext=['avg: '+str(round(constant_value2,1))]*n,
        hoverlabel=dict(font_color='white',bgcolor=px.colors.qualitative.Light24[8]),
        showlegend=False
    ))

    # Add vertical line for a constant value
    max_y_coordinate = len(grouped_df['Community'].unique()) - 0.5  # Adjust based on your bar placement

    # Add vertical lines for constant values
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Antique[4]), 
        y0=0, y1=max_y_coordinate,
        x0=constant_value1, x1=constant_value1
    )
    fig.add_shape(
        type="line", line=dict(dash="dash", width=4, color=px.colors.qualitative.Light24[8]), 
        y0=0, y1=max_y_coordinate,
        x0=constant_value2, x1=constant_value2
)

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

def create_vaccine_reasons_scatter_plot(data):
    vax_reason_cols = [col for col in data.columns if 'ceal_vax_reasons_r2' in col]
    community_count = data.groupby('Community').size().reset_index(name='count')
    gender_count = data.groupby('Gender_recoded').size().reset_index(name='count')
    com_agg_df = data.groupby('Community').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_reason_cols}).reset_index()
    gen_agg_df = data.groupby('Gender_recoded').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_reason_cols}).reset_index()
    community_df = pd.merge(com_agg_df, community_count, on='Community')
    community_df['domain'] = 'Community'
    community_df.rename(columns={'Community': 'Category'}, inplace=True)
    gender_df = pd.merge(gen_agg_df, gender_count, on='Gender_recoded')
    gender_df.rename(columns={'Gender_recoded': 'Category'}, inplace=True)
    gender_df['domain'] = 'Gender_recoded'
    result_df = pd.concat([community_df, gender_df], axis=0)

    for col in vax_reason_cols:
        result_df[col] = (result_df[col] / result_df['count'] * 100).round(1)
    replace_dict = {
        'ceal_vax_reasons_r2___1': 'Family Safety',
        'ceal_vax_reasons_r2___2': 'Community Safety',
        'ceal_vax_reasons_r2___3': 'Personal Safety',
        'ceal_vax_reasons_r2___4': 'Chronic Health Problem',
        'ceal_vax_reasons_r2___5': 'Doctor Recommendation',
        'ceal_vax_reasons_r2___6': 'Avoid Severe Illness',
        'ceal_vax_reasons_r2___7': 'Feel Safe Around People',
        'ceal_vax_reasons_r2___8': 'Return to Normalcy',
        'ceal_vax_reasons_r2___9': 'School/Work Requirement',
        'ceal_vax_reasons_r2___10': 'Stop Wearing Masks',
        'ceal_vax_reasons_r2___12': 'Community/Family Expectation',
        'ceal_vax_reasons_r2___x': 'Would Not Vaccinate',
        'ceal_vax_reasons_r2___oth': 'Other'
    }

    # result_df.rename(columns=rename_dict, inplace=True)

    result_df = result_df.drop(columns=['count'])
    melted_df = result_df.melt(id_vars=['domain','Category'], var_name='Reasons', value_name='Values')
    melted_df['Sample size'] = None
    for index, row in melted_df.iterrows():
        melted_df.at[index, 'Sample size'] = data[(data[str(row['domain'])] == row['Category']) & (data[str(row['Reasons'])] == 1)].shape[0]
    melted_df.replace(replace_dict, inplace=True)
    melted_df.replace({"DENVER Urban American Indian/Alaska Native":"American Indian/Alaska Native"}, inplace=True)
    fig_height = melted_df['Category'].nunique()*70 + 100
    print(fig_height)
    fig = px.scatter(melted_df, y='Category', x='Reasons', size='Values', color='Values', custom_data=['Sample size'],
                      size_max=20, color_continuous_scale=['green', 'yellow', 'red'])
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0), height=fig_height)
    fig.update_traces(hovertemplate='Percentage: %{marker.size}<br>Sample size: %{customdata[0]}')
    fig.update_xaxes(title_text='', tickangle=-45)
    fig.update_yaxes(title_text='')

    return fig

def create_vaccine_concerns_scatter_plot(data):
    vax_concerns_cols = [col for col in data.columns if 'ceal_vax_concerns_r2' in col]
    vax_concerns_cols.remove('ceal_vax_concerns_r2___oth')
    data = data[(data['ceal2_covid_vaxdose']!=1) & (data['ceal2_covid_vaxdose']!=2) & (data['ceal2_covid_vaxdose']!=3)]
    community_count = data.groupby('Community').size().reset_index(name='count')
    gender_count = data.groupby('Gender_recoded').size().reset_index(name='count')
    com_agg_df = data.groupby('Community').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_concerns_cols}).reset_index()
    gen_agg_df = data.groupby('Gender_recoded').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_concerns_cols}).reset_index()
    community_df = pd.merge(com_agg_df, community_count, on='Community')
    community_df['domain'] = 'Community'
    community_df.rename(columns={'Community': 'Category'}, inplace=True)
    gender_df = pd.merge(gen_agg_df, gender_count, on='Gender_recoded')
    gender_df.rename(columns={'Gender_recoded': 'Category'}, inplace=True)
    gender_df['domain'] = 'Gender_recoded'
    result_df = pd.concat([community_df, gender_df], axis=0)

    for col in vax_concerns_cols:
        result_df[col] = (result_df[col] / result_df['count'] * 100).round(1)
    replace_dict = {
    'ceal_vax_concerns_r2___1': 'Allergic to Vaccines',
    'ceal_vax_concerns_r2___2': 'Dislike Needles',
    'ceal_vax_concerns_r2___22': 'Not at Risk',
    'ceal_vax_concerns_r2___3': 'Not Concerned About Illness',
    'ceal_vax_concerns_r2___4': 'Concerned About Side Effects',
    'ceal_vax_concerns_r2___5': 'Doubts on Vaccine Efficacy',
    'ceal_vax_concerns_r2___6': 'Safety Concerns',
    'ceal_vax_concerns_r2___7': 'Pandemic Severity Doubts',
    'ceal_vax_concerns_r2___9': 'Insufficient Information on Vaccine',
    'ceal_vax_concerns_r2___11': 'Concerns About Fetal Cells',
    'ceal_vax_concerns_r2___12': 'Concerns About Infertility',
    'ceal_vax_concerns_r2___13r2': 'Already Had COVID-19',
    'ceal_vax_concerns_r2___14': 'Fear of Getting COVID-19 From Vaccine',
    'ceal_vax_concerns_r2___15': 'Concerns About DNA Change',
    'ceal_vax_concerns_r2___17': 'Trust Issues With Vaccine Source',
    'ceal_vax_concerns_r2___18r2a': 'Concerns About Showing ID',
    'ceal_vax_concerns_r2___21r2': 'Religious Conflicts',
    'ceal_vax_concerns_r2___23': 'Family/Community Disapproval',
    'ceal_vax_concerns_r2___24': 'Fear of Infection at Vaccination Location'
}
    # result_df.rename(columns=rename_dict, inplace=True)

    result_df = result_df.drop(columns=['count'])
    melted_df = result_df.melt(id_vars=['domain','Category'], var_name='Concerns', value_name='Values')
    melted_df['Sample size'] = None
    for index, row in melted_df.iterrows():
        melted_df.at[index, 'Sample size'] = data[(data[str(row['domain'])] == row['Category']) & (data[str(row['Concerns'])] == 1)].shape[0]
    melted_df.replace(replace_dict, inplace=True)
    melted_df.replace({"DENVER Urban American Indian/Alaska Native":"American Indian/Alaska Native"}, inplace=True)
    fig_height = melted_df['Category'].nunique()*70 + 100
    print(fig_height)
    fig = px.scatter(melted_df, y='Category', x='Concerns', size='Values', color='Values', custom_data=['Sample size'],
                      size_max=20, color_continuous_scale=['green', 'yellow', 'red'])
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0), height=fig_height)
    fig.update_traces(hovertemplate='Percentage: %{marker.size}<br>Sample size: %{customdata[0]}')
    fig.update_xaxes(title_text='', tickangle=-45)
    fig.update_yaxes(title_text='')

    return fig

def create_vaccine_challenges_scatter_plot(data):
    vax_challenges_cols = [col for col in data.columns if 'ceal2_vax_challngs' in col]
    vax_challenges_cols.remove('ceal2_vax_challngs___oth')
    data = data[(data['ceal2_covid_vaxdose']==1) | (data['ceal2_covid_vaxdose']==2) | (data['ceal2_covid_vaxdose']==3)]
    community_count = data.groupby('Community').size().reset_index(name='count')
    gender_count = data.groupby('Gender_recoded').size().reset_index(name='count')
    com_agg_df = data.groupby('Community').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_challenges_cols}).reset_index()
    gen_agg_df = data.groupby('Gender_recoded').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_challenges_cols}).reset_index()
    community_df = pd.merge(com_agg_df, community_count, on='Community')
    community_df['domain'] = 'Community'
    community_df.rename(columns={'Community': 'Category'}, inplace=True)
    gender_df = pd.merge(gen_agg_df, gender_count, on='Gender_recoded')
    gender_df.rename(columns={'Gender_recoded': 'Category'}, inplace=True)
    gender_df['domain'] = 'Gender_recoded'
    result_df = pd.concat([community_df, gender_df], axis=0)

    for col in vax_challenges_cols:
        result_df[col] = (result_df[col] / result_df['count'] * 100).round(1)
    replace_dict = {
    'ceal2_vax_challngs___20r2b': 'Did not know how to get an appointment',
    'ceal2_vax_challngs___28': 'Appointment took too long',
    'ceal2_vax_challngs___18r2a': 'Worried about showing ID',
    'ceal2_vax_challngs___19r2a': 'No transportation',
    'ceal2_vax_challngs___19r2b': 'Locations too far',
    'ceal2_vax_challngs___20r2a': 'Did not know where to go',
    'ceal2_vax_challngs___25': 'No childcare',
    'ceal2_vax_challngs___16r2': 'Could not take time off work',
    'ceal2_vax_challngs___26': 'Language barrier at location',
    'ceal2_vax_challngs___27': 'No information in preferred language',
    'ceal2_vax_challngs___6': 'Safety concerns',
    'ceal2_vax_challngs___24': 'Fear of infection at location',
    'ceal2_vax_challngs___4r2': 'Concerned about side effects',
    'ceal2_vax_challngs___5': 'Doubts on vaccine efficacy',
    'ceal2_vax_challngs___1': 'Allergic to vaccines',
    'ceal2_vax_challngs___2': 'Dislike needles',
    'ceal2_vax_challngs___21r2': 'Religious conflicts',
    'ceal2_vax_challngs___23': 'Disapproval from important people',
    'ceal2_vax_challngs___x': 'None',
    'ceal2_vax_challngs___29':'Could not take time off work'
}
    # result_df.rename(columns=rename_dict, inplace=True)

    result_df = result_df.drop(columns=['count'])
    melted_df = result_df.melt(id_vars=['domain','Category'], var_name='Challenges', value_name='Values')
    melted_df['Sample size'] = None
    for index, row in melted_df.iterrows():
        melted_df.at[index, 'Sample size'] = data[(data[str(row['domain'])] == row['Category']) & (data[str(row['Challenges'])] == 1)].shape[0]
    melted_df.replace(replace_dict, inplace=True)
    melted_df.replace({"DENVER Urban American Indian/Alaska Native":"American Indian/Alaska Native"}, inplace=True)
    fig_height = melted_df['Category'].nunique()*70 + 100
    print(fig_height)
    fig = px.scatter(melted_df, y='Category', x='Challenges', size='Values', color='Values', custom_data=['Sample size'],
                      size_max=20, color_continuous_scale=['green', 'yellow', 'red'])
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0), height=fig_height)
    fig.update_traces(hovertemplate='Percentage: %{marker.size}<br>Sample size: %{customdata[0]}')
    fig.update_xaxes(title_text='', tickangle=-45)
    fig.update_yaxes(title_text='')

    return fig

def  create_vaccine_barriers_scatter_plot(data):
    vax_barriers_cols = [col for col in data.columns if 'ceal2_vax_barriers' in col]
    vax_barriers_cols.remove('ceal2_vax_barriers___oth')
    data = data[(data['ceal2_covid_vaxdose']!=1) & (data['ceal2_covid_vaxdose']!=2) & (data['ceal2_covid_vaxdose']!=3)]
    community_count = data.groupby('Community').size().reset_index(name='count')
    gender_count = data.groupby('Gender_recoded').size().reset_index(name='count')
    com_agg_df = data.groupby('Community').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_barriers_cols}).reset_index()
    gen_agg_df = data.groupby('Gender_recoded').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_barriers_cols}).reset_index()
    community_df = pd.merge(com_agg_df, community_count, on='Community')
    community_df['domain'] = 'Community'
    community_df.rename(columns={'Community': 'Category'}, inplace=True)
    gender_df = pd.merge(gen_agg_df, gender_count, on='Gender_recoded')
    gender_df.rename(columns={'Gender_recoded': 'Category'}, inplace=True)
    gender_df['domain'] = 'Gender_recoded'
    result_df = pd.concat([community_df, gender_df], axis=0)

    for col in vax_barriers_cols:
        result_df[col] = (result_df[col] / result_df['count'] * 100).round(1)
    replace_dict = {
        'ceal2_vax_barriers___8r2': 'Cannot afford it',
        'ceal2_vax_barriers___20r2a': 'Do not know where to get vaccinated',
        'ceal2_vax_barriers___19r2a': 'No transportation',
        'ceal2_vax_barriers___19r2b': 'Locations too far or hard to get to',
        'ceal2_vax_barriers___16r2': 'Cannot take time off work',
        'ceal2_vax_barriers___20r2b': 'Do not know how to make an appointment',
        'ceal2_vax_barriers___25': 'No childcare',
        'ceal2_vax_barriers___26': 'Language barrier at location',
        'ceal2_vax_barriers___18r2b': 'No social security number or government issued ID',
        'ceal2_vax_barriers___x': 'None'
    }
    # result_df.rename(columns=rename_dict, inplace=True)

    result_df = result_df.drop(columns=['count'])
    melted_df = result_df.melt(id_vars=['domain','Category'], var_name='Barriers', value_name='Values')
    melted_df['Sample size'] = None
    for index, row in melted_df.iterrows():
        melted_df.at[index, 'Sample size'] = data[(data[str(row['domain'])] == row['Category']) & (data[str(row['Barriers'])] == 1)].shape[0]
    melted_df.replace(replace_dict, inplace=True)
    melted_df.replace({"DENVER Urban American Indian/Alaska Native":"American Indian/Alaska Native"}, inplace=True)
    fig_height = melted_df['Category'].nunique()*70 + 100
    print(fig_height)
    fig = px.scatter(melted_df, y='Category', x='Barriers', size='Values', color='Values', custom_data=['Sample size'],
                      size_max=20, color_continuous_scale=['green', 'yellow', 'red'])
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0), height=fig_height)
    fig.update_traces(hovertemplate='Percentage: %{marker.size}<br>Sample size: %{customdata[0]}')
    fig.update_xaxes(title_text='', tickangle=-45)
    fig.update_yaxes(title_text='')

    return fig

def create_vaccine_reasons_children_scatter_plot(data):
    vax_reasons_ch_cols = [col for col in data.columns if 'vax_reasons_ch_r2' in col]
    vax_reasons_ch_cols.remove('vax_reasons_ch_r2___oth')
    data = data[(data['parent_ch1217'] == 1) | (data['parent_ch511'] == 1) | (data['parent_ch04'] == 1)]
    community_count = data.groupby('Community').size().reset_index(name='count')
    gender_count = data.groupby('Gender_recoded').size().reset_index(name='count')
    com_agg_df = data.groupby('Community').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_reasons_ch_cols}).reset_index()
    gen_agg_df = data.groupby('Gender_recoded').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_reasons_ch_cols}).reset_index()
    community_df = pd.merge(com_agg_df, community_count, on='Community')
    community_df['domain'] = 'Community'
    community_df.rename(columns={'Community': 'Category'}, inplace=True)
    gender_df = pd.merge(gen_agg_df, gender_count, on='Gender_recoded')
    gender_df.rename(columns={'Gender_recoded': 'Category'}, inplace=True)
    gender_df['domain'] = 'Gender_recoded'
    result_df = pd.concat([community_df, gender_df], axis=0)

    for col in vax_reasons_ch_cols:
        result_df[col] = (result_df[col] / result_df['count'] * 100).round(1)
    replace_dict = {
        'vax_reasons_ch_r2___1': 'Keep family safe',
        'vax_reasons_ch_r2___2': 'Keep community safe',
        'vax_reasons_ch_r2___3': 'Keep child safe',
        'vax_reasons_ch_r2___4': 'Child has a chronic health problem',
        'vax_reasons_ch_r2___5': 'Doctor recommendation',
        'vax_reasons_ch_r2___6': 'Prevent severe illness',
        'vax_reasons_ch_r2___7': 'Child feels safe around others',
        'vax_reasons_ch_r2___8': 'Belief in returning to normal',
        'vax_reasons_ch_r2___9': 'School or workplace requirement',
        'vax_reasons_ch_r2___10': 'Child can stop wearing masks',
        'vax_reasons_ch_r2___12': 'Community or family expectations',
        'vax_reasons_ch_r2___x': 'None (Would not vaccinate child)'
    }

    # result_df.rename(columns=rename_dict, inplace=True)

    result_df = result_df.drop(columns=['count'])
    melted_df = result_df.melt(id_vars=['domain','Category'], var_name='Reasons - Children', value_name='Values')
    melted_df['Sample size'] = None
    for index, row in melted_df.iterrows():
        melted_df.at[index, 'Sample size'] = data[(data[str(row['domain'])] == row['Category']) & (data[str(row['Reasons - Children'])] == 1)].shape[0]
    melted_df.replace(replace_dict, inplace=True)
    melted_df.replace({"DENVER Urban American Indian/Alaska Native":"American Indian/Alaska Native"}, inplace=True)
    fig_height = melted_df['Category'].nunique()*70 + 100
    print(fig_height)
    fig = px.scatter(melted_df, y='Category', x='Reasons - Children', size='Values', color='Values', custom_data=['Sample size'],
                      size_max=20, color_continuous_scale=['green', 'yellow', 'red'])
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0), height=fig_height)
    fig.update_traces(hovertemplate='Percentage: %{marker.size}<br>Sample size: %{customdata[0]}')
    fig.update_xaxes(title_text='', tickangle=-45)
    fig.update_yaxes(title_text='')

    return fig

def create_vaccine_concerns_children_5_17_scatter_plot(data):
    vax_concerns_ch_cols = [col for col in data.columns if 'vax_concerns_ch517' in col]
    vax_concerns_ch_cols.remove('vax_concerns_ch517___oth')
    vax_concerns_ch_cols.remove('vax_concerns_ch517_spec')
    data = data[((data['parent_ch1217'] == 1) & (data['covid_vaxdose_ch1217'] != 1) 
                    & (data['covid_vaxdose_ch1217'] != 2) & (data['covid_vaxdose_ch1217'] != 3)) | 
                    ((data['parent_ch511'] == 1) & (data['covid_vaxdose_ch511'] != 1) & 
                     (data['covid_vaxdose_ch511'] != 2) & (data['covid_vaxdose_ch511'] != 3))]
    community_count = data.groupby('Community').size().reset_index(name='count')
    gender_count = data.groupby('Gender_recoded').size().reset_index(name='count')
    com_agg_df = data.groupby('Community').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_concerns_ch_cols}).reset_index()
    gen_agg_df = data.groupby('Gender_recoded').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_concerns_ch_cols}).reset_index()
    community_df = pd.merge(com_agg_df, community_count, on='Community')
    community_df['domain'] = 'Community'
    community_df.rename(columns={'Community': 'Category'}, inplace=True)
    gender_df = pd.merge(gen_agg_df, gender_count, on='Gender_recoded')
    gender_df.rename(columns={'Gender_recoded': 'Category'}, inplace=True)
    gender_df['domain'] = 'Gender_recoded'
    result_df = pd.concat([community_df, gender_df], axis=0)

    for col in vax_concerns_ch_cols:
        result_df[col] = (result_df[col] / result_df['count'] * 100).round(1)
    replace_dict = {
        'vax_concerns_ch517___1': 'Child is allergic to vaccines',
        'vax_concerns_ch517___2': 'Child dislikes needles',
        'vax_concerns_ch517___22': 'Child not at risk',
        'vax_concerns_ch517___3': 'Not concerned about child getting sick',
        'vax_concerns_ch517___4': 'Concerned about side effects',
        'vax_concerns_ch517___5': 'Doubts on vaccine efficacy',
        'vax_concerns_ch517___6': 'Safety concerns',
        'vax_concerns_ch517___7': 'Pandemic severity doubts',
        'vax_concerns_ch517___9': 'Insufficient information on vaccine',
        'vax_concerns_ch517___11': 'Concerns about fetal cells',
        'vax_concerns_ch517___12': 'Concerns about infertility',
        'vax_concerns_ch517___13r2': 'Child already had COVID-19',
        'vax_concerns_ch517___14': 'Fear of getting COVID-19 from vaccine',
        'vax_concerns_ch517___15': 'Concerns about DNA change',
        'vax_concerns_ch517___17': 'Trust issues with vaccine source',
        'vax_concerns_ch517___18r2a': 'Concerns about showing ID',
        'vax_concerns_ch517___21': 'Concerns about school performance',
        'vax_concerns_ch517___31': 'Religious conflicts',
        'vax_concerns_ch517___23': 'Family/Community disapproval',
        'vax_concerns_ch517___24': 'Fear of infection at vaccination location'
    }
    # result_df.rename(columns=rename_dict, inplace=True)

    result_df = result_df.drop(columns=['count'])
    melted_df = result_df.melt(id_vars=['domain','Category'], var_name='Concerns - Children', value_name='Values')
    melted_df['Sample size'] = None
    for index, row in melted_df.iterrows():
        melted_df.at[index, 'Sample size'] = data[(data[str(row['domain'])] == row['Category']) & (data[str(row['Concerns - Children'])] == 1)].shape[0]
    melted_df.replace(replace_dict, inplace=True)
    melted_df.replace({"DENVER Urban American Indian/Alaska Native":"American Indian/Alaska Native"}, inplace=True)
    fig_height = melted_df['Category'].nunique()*70 + 100
    print(fig_height)
    fig = px.scatter(melted_df, y='Category', x='Concerns - Children', size='Values', color='Values', custom_data=['Sample size'],
                      size_max=20, color_continuous_scale=['green', 'yellow', 'red'])
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0), height=fig_height)
    fig.update_traces(hovertemplate='Percentage: %{marker.size}<br>Sample size: %{customdata[0]}')
    fig.update_xaxes(title_text='', tickangle=-45)
    fig.update_yaxes(title_text='')

    return fig

def create_vaccine_concerns_children_4_scatter_plot(data):
    vax_concerns_ch_cols = [col for col in data.columns if 'vax_concerns_ch04' in col]
    vax_concerns_ch_cols.remove('vax_concerns_ch04___oth')
    vax_concerns_ch_cols.remove('vax_concerns_ch04_spec')
    data = data[(data['parent_ch04'] == 1) & (data['parent_ch1217'] != 1) 
                    & (data['parent_ch511'] != 1)]
    community_count = data.groupby('Community').size().reset_index(name='count')
    gender_count = data.groupby('Gender_recoded').size().reset_index(name='count')
    com_agg_df = data.groupby('Community').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_concerns_ch_cols}).reset_index()
    gen_agg_df = data.groupby('Gender_recoded').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_concerns_ch_cols}).reset_index()
    community_df = pd.merge(com_agg_df, community_count, on='Community')
    community_df['domain'] = 'Community'
    community_df.rename(columns={'Community': 'Category'}, inplace=True)
    gender_df = pd.merge(gen_agg_df, gender_count, on='Gender_recoded')
    gender_df.rename(columns={'Gender_recoded': 'Category'}, inplace=True)
    gender_df['domain'] = 'Gender_recoded'
    result_df = pd.concat([community_df, gender_df], axis=0)

    for col in vax_concerns_ch_cols:
        result_df[col] = (result_df[col] / result_df['count'] * 100).round(1)
    replace_dict = {
        'vax_concerns_ch04___1': 'Child is allergic to vaccines',
        'vax_concerns_ch04___2': 'Child dislikes needles',
        'vax_concerns_ch04___22': 'Child not at risk',
        'vax_concerns_ch04___3': 'Not concerned about child getting sick',
        'vax_concerns_ch04___4': 'Concerned about side effects',
        'vax_concerns_ch04___5': 'Doubts on vaccine efficacy',
        'vax_concerns_ch04___6': 'Safety concerns',
        'vax_concerns_ch04___7': 'Pandemic severity doubts',
        'vax_concerns_ch04___8': 'Do not want to pay for it',
        'vax_concerns_ch04___9': 'Insufficient information on vaccine',
        'vax_concerns_ch04___11': 'Concerns about fetal cells',
        'vax_concerns_ch04___12': 'Concerns about infertility',
        'vax_concerns_ch04___13r2': 'Child already had COVID-19',
        'vax_concerns_ch04___14': 'Fear of getting COVID-19 from vaccine',
        'vax_concerns_ch04___15': 'Concerns about DNA change',
        'vax_concerns_ch04___16r2': 'Cannot take time off work',
        'vax_concerns_ch04___17': 'Trust issues with vaccine source',
        'vax_concerns_ch04___18r2a': 'Concerns about showing ID',
        'vax_concerns_ch04___18r2b': 'No social security number or government issued ID',
        'vax_concerns_ch04___19r2a': 'No transportation',
        'vax_concerns_ch04___19r2b': 'Locations too far or hard to get to',
        'vax_concerns_ch04___20r2a': 'Do not know where to go for vaccination',
        'vax_concerns_ch04___20r2b': 'Do not know how to get an appointment',
        'vax_concerns_ch04___21': 'Concerns about school performance',
        'vax_concerns_ch04___31': 'Religious conflicts',
        'vax_concerns_ch04___23': 'Family/Community disapproval',
        'vax_concerns_ch04___24': 'Fear of infection at vaccination location',
        'vax_concerns_ch04___25': 'No childcare',
        'vax_concerns_ch04___26': 'Language barrier at location',
        'vax_concerns_ch04___x': 'None'
    }

    result_df = result_df.drop(columns=['count'])
    melted_df = result_df.melt(id_vars=['domain','Category'], var_name='Concerns - Children', value_name='Values')
    melted_df['Sample size'] = None
    for index, row in melted_df.iterrows():
        melted_df.at[index, 'Sample size'] = data[(data[str(row['domain'])] == row['Category']) & (data[str(row['Concerns - Children'])] == 1)].shape[0]
    melted_df.replace(replace_dict, inplace=True)
    melted_df.replace({"DENVER Urban American Indian/Alaska Native":"American Indian/Alaska Native"}, inplace=True)
    fig_height = melted_df['Category'].nunique()*70 + 100
    print(fig_height)
    fig = px.scatter(melted_df, y='Category', x='Concerns - Children', size='Values', color='Values', custom_data=['Sample size'],
                      size_max=20, color_continuous_scale=['green', 'yellow', 'red'])
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0), height=fig_height)
    fig.update_traces(hovertemplate='Percentage: %{marker.size}<br>Sample size: %{customdata[0]}')
    fig.update_xaxes(title_text='', tickangle=-45)
    fig.update_yaxes(title_text='')

    return fig

def create_vaccine_challenges_children_5_17_scatter_plot(data):
    vax_challenges_ch_cols = [col for col in data.columns if 'vax_challngs_ch517' in col]
    vax_challenges_ch_cols.remove('vax_challngs_ch517___oth')
    vax_challenges_ch_cols.remove('vax_challngs_ch517_spec')
    data = data[((data['parent_ch1217'] == 1) & ((data['covid_vaxdose_ch1217'] == 1) | 
            (data['covid_vaxdose_ch1217'] == 2) | (data['covid_vaxdose_ch1217'] == 3)) & 
            (data['parent_ch511'] == 0)) | ((data['parent_ch511'] == 1) & 
            ((data['covid_vaxdose_ch511'] == 1) | (data['covid_vaxdose_ch511'] == 2) | 
             (data['covid_vaxdose_ch511'] == 3)) & (data['parent_ch1217'] == 0)) | 
             ((data['parent_ch1217'] == 1) & ((data['covid_vaxdose_ch1217'] == 1) | 
            (data['covid_vaxdose_ch1217'] == 2) | (data['covid_vaxdose_ch1217'] == 3)) & 
            (data['parent_ch511'] == 1) & ((data['covid_vaxdose_ch511'] == 1) | 
            (data['covid_vaxdose_ch511'] == 2) | (data['covid_vaxdose_ch511'] == 3)))]
    community_count = data.groupby('Community').size().reset_index(name='count')
    gender_count = data.groupby('Gender_recoded').size().reset_index(name='count')
    com_agg_df = data.groupby('Community').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_challenges_ch_cols}).reset_index()
    gen_agg_df = data.groupby('Gender_recoded').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_challenges_ch_cols}).reset_index()
    community_df = pd.merge(com_agg_df, community_count, on='Community')
    community_df['domain'] = 'Community'
    community_df.rename(columns={'Community': 'Category'}, inplace=True)
    gender_df = pd.merge(gen_agg_df, gender_count, on='Gender_recoded')
    gender_df.rename(columns={'Gender_recoded': 'Category'}, inplace=True)
    gender_df['domain'] = 'Gender_recoded'
    result_df = pd.concat([community_df, gender_df], axis=0)

    for col in vax_challenges_ch_cols:
        result_df[col] = (result_df[col] / result_df['count'] * 100).round(1)
    replace_dict = {
    'vax_challngs_ch517___20r2b': 'Did not know how to get an appointment',
    'vax_challngs_ch517___28': 'Appointment took too long',
    'vax_challngs_ch517___18r2a': 'Worried about showing ID',
    'vax_challngs_ch517___19r2a': 'No transportation',
    'vax_challngs_ch517___19r2b': 'Locations too far',
    'vax_challngs_ch517___20r2a': 'Did not know where to go',
    'vax_challngs_ch517___25': 'No childcare',
    'vax_challngs_ch517___16r2': 'Could not take time off work',
    'vax_challngs_ch517___26': 'Language barrier at location',
    'vax_challngs_ch517___27': 'No information in preferred language',
    'vax_challngs_ch517___6': 'Safety concerns',
    'vax_challngs_ch517___24': 'Fear of infection at location',
    'vax_challngs_ch517___4r2': 'Concerned about side effects',
    'vax_challngs_ch517___5': 'Doubts on vaccine efficacy',
    'vax_challngs_ch517___1': 'Child is allergic to vaccines',
    'vax_challngs_ch517___2': 'Child dislikes needles',
    'vax_challngs_ch517___31': 'Religious conflicts',
    'vax_challngs_ch517___23': 'Disapproval from important people',
    'vax_challngs_ch517___x': 'None',
    'vax_challngs_ch517___19r2aa': 'No transportation'
}

    result_df = result_df.drop(columns=['count'])
    melted_df = result_df.melt(id_vars=['domain','Category'], var_name='Challenges - Children', value_name='Values')
    melted_df['Sample size'] = None
    for index, row in melted_df.iterrows():
        melted_df.at[index, 'Sample size'] = data[(data[str(row['domain'])] == row['Category']) & (data[str(row['Challenges - Children'])] == 1)].shape[0]
    melted_df.replace(replace_dict, inplace=True)
    melted_df.replace({"DENVER Urban American Indian/Alaska Native":"American Indian/Alaska Native"}, inplace=True)
    fig_height = melted_df['Category'].nunique()*70 + 100
    print(fig_height)
    fig = px.scatter(melted_df, y='Category', x='Challenges - Children', size='Values', color='Values', custom_data=['Sample size'],
                      size_max=20, color_continuous_scale=['green', 'yellow', 'red'])
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0), height=fig_height)
    fig.update_traces(hovertemplate='Percentage: %{marker.size}<br>Sample size: %{customdata[0]}')
    fig.update_xaxes(title_text='', tickangle=-45)
    fig.update_yaxes(title_text='')

    return fig

def create_vaccine_barriers_children_scatter_plot(data):
    vax_barriers_ch_cols = [col for col in data.columns if 'vax_barriers_ch517' in col]
    vax_barriers_ch_cols.remove('vax_barriers_ch517___oth')
    vax_barriers_ch_cols.remove('vax_barriers_ch517_spec')
    data = data[((data['parent_ch1217'] == 1) & (data['covid_vaxdose_ch1217'] != 1) & (data['covid_vaxdose_ch1217'] != 2)
              & (data['covid_vaxdose_ch1217'] != 3)) | ((data['parent_ch511'] == 1) & (data['covid_vaxdose_ch511'] != 1)
             & (data['covid_vaxdose_ch511'] != 2) & (data['covid_vaxdose_ch511'] != 3))]
    community_count = data.groupby('Community').size().reset_index(name='count')
    gender_count = data.groupby('Gender_recoded').size().reset_index(name='count')
    com_agg_df = data.groupby('Community').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_barriers_ch_cols}).reset_index()
    gen_agg_df = data.groupby('Gender_recoded').agg(**{col: (col, lambda x: (x==1).sum()) for col in vax_barriers_ch_cols}).reset_index()
    community_df = pd.merge(com_agg_df, community_count, on='Community')
    community_df['domain'] = 'Community'
    community_df.rename(columns={'Community': 'Category'}, inplace=True)
    gender_df = pd.merge(gen_agg_df, gender_count, on='Gender_recoded')
    gender_df.rename(columns={'Gender_recoded': 'Category'}, inplace=True)
    gender_df['domain'] = 'Gender_recoded'
    result_df = pd.concat([community_df, gender_df], axis=0)

    for col in vax_barriers_ch_cols:
        result_df[col] = (result_df[col] / result_df['count'] * 100).round(1)
    replace_dict = {
        'vax_barriers_ch517___8r2': 'Cannot pay for it',
        'vax_barriers_ch517___20r2a': 'Do not know where to get child vaccinated',
        'vax_barriers_ch517___19r2a': 'No transportation',
        'vax_barriers_ch517___19r2b': 'Locations too far or hard to get to',
        'vax_barriers_ch517___16r2': 'Cannot take time off work',
        'vax_barriers_ch517___20r2b': 'Do not know how to make an appointment',
        'vax_barriers_ch517___25': 'No childcare',
        'vax_barriers_ch517___26': 'Language barrier at location',
        'vax_barriers_ch517___18r2b': 'No social security number or government issued ID',
        'vax_barriers_ch517___x': 'None'
    }

    result_df = result_df.drop(columns=['count'])
    melted_df = result_df.melt(id_vars=['domain','Category'], var_name='Barriers - Children', value_name='Values')
    melted_df['Sample size'] = None
    for index, row in melted_df.iterrows():
        melted_df.at[index, 'Sample size'] = data[(data[str(row['domain'])] == row['Category']) & (data[str(row['Barriers - Children'])] == 1)].shape[0]
    melted_df.replace(replace_dict, inplace=True)
    melted_df.replace({"DENVER Urban American Indian/Alaska Native":"American Indian/Alaska Native"}, inplace=True)
    fig_height = melted_df['Category'].nunique()*70 + 100
    print(fig_height)
    fig = px.scatter(melted_df, y='Category', x='Barriers - Children', size='Values', color='Values', custom_data=['Sample size'],
                      size_max=20, color_continuous_scale=['green', 'yellow', 'red'])
    fig.update_layout(autosize=True, margin=dict(l=0, r=0, b=0, t=0), height=fig_height)
    fig.update_traces(hovertemplate='Percentage: %{marker.size}<br>Sample size: %{customdata[0]}')
    fig.update_xaxes(title_text='', tickangle=-45)
    fig.update_yaxes(title_text='')

    return fig