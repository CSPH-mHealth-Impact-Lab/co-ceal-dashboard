import plotly.express as px
import plotly.graph_objects as go
import os
from dash import html, dcc
import numpy as np

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

import plotly.express as px

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
        hovertemplate="Count: %{x}<br>Percentage: %{percent}<extra></extra> "
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

    fig.update_traces(texttemplate='%{text}', textposition='outside')

    return fig


