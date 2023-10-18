import plotly.express as px
import os
from dash import html, dcc

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
def create_histogram(data, column,title_text,num_bins=10,graph_title_font_color=graph_title_font_color, graph_title_font_size=graph_title_font_size):
    fig = px.histogram(data, x=column, nbins=num_bins, labels={'Age': 'Age'})
    
    # Customize the appearance of the histogram
    fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)
    
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
    fig = px.pie(data, names=category_column, values=count_column, title=title_text)
    
    # Customize the appearance of the pie chart
    # fig.update_traces(marker_colors=['rgb(158,202,225)', 'rgb(255,133,27)', 'rgb(139,204,93)'])
    
    # Customize the title, font, and layout settings directly
    fig.update_layout(
        title_font=dict(size=graph_title_font_size, color=graph_title_font_color),
        title_x=0.5,  # Center align the title horizontally
        title_y=0.95  # Adjust the vertical position of the title
    )
    
    return fig