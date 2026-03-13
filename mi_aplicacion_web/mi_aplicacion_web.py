"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", size="9"),

        ),
    )


app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="grass", # Verde por defecto para botones y badges
        radius="medium"
    ),
    head_components=[
        rx.el.link(rel="icon", href="/logo_app.png", type_="image/png")
    ]
)

app.add_page(index)

