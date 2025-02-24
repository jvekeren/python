import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 15, 30]
}
df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1("Simple Dashboard"),
    
    dcc.Graph(
        id='bar-chart',
        figure=px.bar(df, x='Category', y='Values', title='Bar Chart')
    ),
    
    dcc.Graph(
        id='pie-chart',
        figure=px.pie(df, values='Values', names='Category', title='Pie Chart')
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
