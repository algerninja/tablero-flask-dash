from dash import Dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import numpy as np
import pandas as pd

from flask_login import current_user
from flask import session


def init_dashboard(server):

    dash_app = Dash(server=server, url_base_pathname='/dash/',
                    external_stylesheets=[dbc.themes.BOOTSTRAP])

    dash_app.scripts.config.serve_locally = True

    search_bar = dbc.Row(
        [
            html.Ul([
                html.Li(html.A(dbc.Row(
                    dbc.Col(dbc.NavItem('Home', className='ml-2')), no_gutters=True),
                    href='/home', className='nav-link'), className='nav-item active' ),

                html.Li(html.A(dbc.Row(
                    dbc.Col(dbc.NavItem('Dash', className='ml-2')), no_gutters=True),
                    href='/dash', className='nav-link'), className='nav-item'),
                html.Li(html.A(
                    dbc.Row(
                        dbc.Col(dbc.NavItem('Log In', className='ml-2')), no_gutters=True),
                    href='/login', className='nav-link'), className='nav-item'),
                html.Li(html.A(
                    dbc.Row(
                        dbc.Col(dbc.NavItem('Log Out', className='ml-2')), no_gutters=True),
                    href='/logout', className='nav-link'), className='nav-item'),
            ], className='navbar-nav'),

        ]
    )

    dash_app.layout = html.Div([



        dbc.Navbar(
            [
                html.A(
                    dbc.Row(dbc.Col(dbc.NavbarBrand("App name", className="ml-2")),
                            no_gutters=True,
                            ),
                    href="/home",
                ),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(search_bar, id="navbar-collapse", navbar=True),
            ],
            color="dark",
            dark=True
        )
    ])

    init_callbacks(dash_app)

    return dash_app.server


def init_callbacks(dash_app):
    @dash_app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")],
    )
    def toggle_navbar_collapse(n, is_open):
        if n:
            return not is_open
        return is_open
