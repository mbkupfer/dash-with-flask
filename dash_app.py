from flask import Flask
import dash 
import dash_core_components as dcc
import dash_html_components as html

server = Flask(__name__)
app = dash.Dash(__name__, server = server)
app.config.requests_pathname_prefix = ''

app.layout = html.Div(
    html.H1('Dash application')
)

@server.route('/')
def myDashApp():
    return app.index()

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
