import reflex as rx
from .estructura_de_menu import encabezado, menu_lateral

def contenido() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Reportes"),
            rx.badge("Contenido de Reportes"),
            rx.box(
                width="200px",
                height="200px",
                bg="red",
                padding="20px",
            ),
            spacing="3"
        ),
        width="100%"
    )

@rx.page(route="/reportes", title="Reportes")
def reportes() -> rx.Component:
    return rx.vstack(
        encabezado(),
        rx.hstack(
            menu_lateral(),
            contenido(),
            width="100%"
        ),
        spacing="0"
    )