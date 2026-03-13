import reflex as rx
from .estructura_de_menu import encabezado, menu_lateral

def contenido() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Documentos"),
            rx.badge("Contenido de Documentos"),
            spacing="3"
        ),
        width="100%"
    )

@rx.page(route="/documentos", title="Documentos")
def documentos() -> rx.Component:
    return rx.vstack(
        encabezado(),
        rx.hstack(
            menu_lateral(),
            contenido(),
            width="100%"
        ),
        spacing="0"
    )