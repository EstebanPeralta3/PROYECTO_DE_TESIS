import reflex as rx
from .estructura_de_menu import encabezado, menu_lateral

def contenido() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Formularios"),
            rx.badge("Contenido de Formularios"),
            spacing="3"
        ),
        width="100%"
    )

@rx.page(route="/formularios", title="Formularios")
def formularios() -> rx.Component:
    return rx.vstack(
        encabezado(),
        rx.hstack(
            menu_lateral(),
            contenido(),
            width="100%"
        ),
        spacing="0"
    )