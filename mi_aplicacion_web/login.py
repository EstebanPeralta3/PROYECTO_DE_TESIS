import reflex as rx

@rx.page(route="/login", title="Login")
def login() -> rx.Component:
    return rx.center(
            rx.vstack(
                rx.card(
                    rx.form(
                        rx.vstack(
                            rx.image(src="/logo_app.png",
                            width="150px",
                            height="150px",
                            border_radius="30% 70% 70% 30% / 30% 30% 70% 70%"
                            ),
                            rx.heading("JBZ Docʼs", align="center", padding="2", color="#064e3b"),
                            rx.text("Inicio de sesión"),
                            rx.hstack(
                                rx.icon("user"),
                                rx.input(placeholder="usuario", type="text")
                                ),
                            rx.hstack(
                                rx.icon("key-round"),
                                rx.input(placeholder="contraseña", type="password"),
                            ),
                            rx.button("Ingresar", color_scheme="grass", variant="ghost", type="submit"),
                            spacing="3",
                            align="center"
                        ),
                    ),
                    padding="6",
                    width="400px",
                ),
            rx.text(rx.link("Recuperar contraseña", color_scheme="blue"), size="1"),
            align="end",
            spacing="6",
        ),
        height="100vh"
    )