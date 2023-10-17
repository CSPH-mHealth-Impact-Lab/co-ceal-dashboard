import dash_bootstrap_components as dbc
from dash import html, dcc

nav_items = [
    dbc.NavItem(dbc.NavLink("Wave 1", href="#")),
    dbc.NavItem(dbc.NavLink("Wave 2", href="#")),
    dbc.NavItem(dbc.NavLink("Wave 3", href="#")),
    dbc.DropdownMenu(
        label="Cross Wave Analysis",  # Dropdown label
        children=[
            dbc.DropdownMenuItem("Option 4", href="#"),
            dbc.DropdownMenuItem("Option 5", href="#"),
            dbc.DropdownMenuItem("Option 6", href="#"),
        ],
    ),
]

Navbar = dbc.NavbarSimple(
        children=nav_items,
        brand="CO-CEAL DASHBOARD",
        brand_href="#",
        id="navbar",
        className="navbar navbar-expand-lg navbar-dark bg-dark p-1 m-1",
    )