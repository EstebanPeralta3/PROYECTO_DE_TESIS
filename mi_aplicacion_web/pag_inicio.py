import reflex as rx
from .estructura_de_menu import encabezado, menu_lateral

def contenido() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Inicio"),
            rx.badge("Este es el contenido"),
            spacing="3"
        ),
        padding="6",
        width="100%"
    )

@rx.page(route="/inicio", title="inicio")
def inicio() -> rx.Component:
    return rx.vstack(
        encabezado(),
        rx.hstack(
            menu_lateral(),
            contenido(),
            width="100%"
        ),
        spacing="0"
    )