import dash_bootstrap_components as dbc
from dash import html, dcc

nav_items = [
    dbc.NavItem(dbc.NavLink("Wave 1", href="/")),
    dbc.NavItem(dbc.NavLink("Wave 2", href="/wave-2")),
    dbc.NavItem(dbc.NavLink("Wave 3", href="/wave-3")),
    dbc.DropdownMenu(
        label="Cross Wave Analysis",  # Dropdown label
        children=[
            dbc.DropdownMenuItem("Change from wave 1 to 2", href="/wave-1-2"),
            dbc.DropdownMenuItem("Change from wave 2 to 3", href="/wave-2-3"),
            dbc.DropdownMenuItem("Change from wave 1 to 3", href="/wave-1-3"),
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