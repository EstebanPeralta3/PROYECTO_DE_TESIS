import reflex as rx

def notificacion_de_error(mensaje: str, icono:str, color:str) -> rx.Component:
    return rx.callout(
        mensaje,
        icon=icono,
        color_scheme=color,
        variant="soft",
        style=estilo
    )

estilo = {
        "position": "fixed",
        "bottom": "20px",
        "right": "20px",
        "z_index": "9999",
        "width": "300px",
        "box_shadow": "0 4px 12px rgba(0,0,0,0.15)",
    }