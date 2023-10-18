import plotly.express as px
from plotly import graph_objs as go
import os
from dash import html, dcc
import numpy as np

graph_title_font_color = os.environ.get("graph_title_font_color", "#333")
graph_title_font_size = int(os.environ.get("graph_title_font_size", 18))

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

# Function to create a pie chart with updated layout
def create_pie_chart(data, category_column, count_column, title_text, graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    data_cleaned = data.dropna(subset=[category_column])
    fig = px.pie(data_cleaned, names=category_column, values=count_column, title=title_text)
    
    # Customize the appearance of the pie chart
    # fig.update_traces(marker_colors=['rgb(158,202,225)', 'rgb(255,133,27)', 'rgb(139,204,93)'])
    
    # Customize the title, font, and layout settings directly
    fig.update_layout(
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95  # Adjust the vertical position of the title
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
    counts['Percentage'] = (counts['Count'] / len(data_cleaned)) * 100
    counts['Percentage'] = counts['Percentage'].round(1)

    # Create a horizontal bar chart
    fig = px.bar(
        counts,
        x='Percentage',
        y=column,
        text='Percentage',
        title=title_text,
        labels={'Percentage': 'Percentage (%)', column: column},
        orientation='h'  # Make it a horizontal bar chart
    )

    # Customize the appearance of the chart
    fig.update_traces(marker_color='rgb(153, 102, 204)', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.9)

    # Customize the font and layout settings
    fig.update_layout(
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        xaxis_title='Percentage (%)',  # Change x-axis label
        yaxis_title='',  # Hide y-axis label
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95,  # Adjust the vertical position of the title
        xaxis=dict(range=[0, 100])  # Set x-axis scale from 0 to 100%
    )

    # Update the annotations font color
    fig.update_annotations(textfont_color="#333")  # Make annotations font color darker

    return fig
