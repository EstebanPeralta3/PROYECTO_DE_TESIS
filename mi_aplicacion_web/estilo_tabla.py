import reflex as rx

# Configuración de colores y formas
BG_DARK_GREEN = "#064e3b"
LIGHT_GREEN_HOVER = "#f0fdf4"  # Un verde muy sutil para las filas
BORDER_COLOR = "#e5e7eb"

style_table = {
    "width": "100%",
    "border_radius": "10px",
    "overflow": "hidden",
    "border": f"1px solid {BORDER_COLOR}",
    "box_shadow": "0 4px 6px -1px rgba(0, 0, 0, 0.1)",
}

style_header = {
    "bg": BG_DARK_GREEN,
    "color": "white",
    "font_weight": "bold",
    "text_transform": "uppercase",
    "font_size": "0.85em",
    "letter_spacing": "0.05em",
}

style_row = {
    "_hover": {"bg": LIGHT_GREEN_HOVER},
    "transition": "background 0.2s ease",
}