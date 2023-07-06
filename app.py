import pandas as pd
import plotly.express as px
import dash
from dash import html, dcc

# Read the data from the CSV file, skipping problematic lines
try:
    data = pd.read_csv(
        'https://raw.githubusercontent.com/chriszapp/datasets/main/books.csv', error_bad_lines=False)
except pd.errors.ParserError as e:
    print(f"Error reading CSV: {str(e)}")
    exit(1)

# Create the Dash app
app = dash.Dash(__name__)
server = app.server 

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1("Book Data Visualization"),
        dcc.Dropdown(
            id="x-variable",
            options=[{'label': col, 'value': col} for col in data.columns],
            value=data.columns[0]  # Set the default value
        ),
        dcc.Dropdown(
            id="y-variable",
            options=[{'label': col, 'value': col} for col in data.columns],
            value=data.columns[1]  # Set the default value
        ),
        dcc.Graph(id="graph")
    ]
)

# Define the callback function for updating the graph


@app.callback(
    dash.dependencies.Output("graph", "figure"),
    [dash.dependencies.Input("x-variable", "value"),
     dash.dependencies.Input("y-variable", "value")]
)
def update_graph(x_variable, y_variable):
    fig = px.scatter(data, x=x_variable, y=y_variable, title="Book Data")
    return fig


# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
