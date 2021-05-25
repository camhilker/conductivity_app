# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data.tsv', delimiter='\t')

fig = px.scatter(df, x="Test_Day", y="Conductivity(mS/cm)", color="Conductivity_User", hover_data=["Calibration_User", "ERB_133X_Lot"])

fig.update_traces(marker=dict(size=12),
                  selector=dict(mode='markers'))

fig_2 = px.box(df, x="ERB_133X_Lot", y="Conductivity(mS/cm)")

app.layout = html.Div(children=[
    html.H1(children='Conductivity User by Day'),

    html.Div(children='''
        Hover over points to see Calibration User and Lot Number
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    
    html.H1(children='Conductivity User by Lot Number'),
    
    dcc.Graph(
        id='example-graph-2',
        figure=fig_2
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
