import reflex as rx

# Funcion que retorna un componente
def encabezado() -> rx.Component:
        # Componente caja                       
    return rx.box(   
            # Componente que agrupa de forma vertical                                      
            rx.hstack(
                # Link el cual contiene un header, al hacer click, lleva a la pagina principal                               
                rx.link(                                
                    rx.heading(
                        "JBZ Docʼs", 
                        color="white", 
                        justify_content="center"
                        ), 
                    href="/inicio", 
                    underline="none"
                    ),
                width="100vw",
                height="10vh",
                bg="#064e3b",
                spacing="6",
                padding="20px",
                ),
            text_align="start"
            ),

def menu_lateral() -> rx.Component:
    return rx.vstack(
                rx.separator(),
                rx.link(
                    rx.button(
                        rx.icon(
                            "monitor-cog"
                            ), 
                        "Aministración", 
                        width="100%",
                        height="40px",
                        variant="ghost", 
                        radius="none", 
                        justify_content="start", 
                        color="white"
                    ),
                    href="/administracion",
                    width="100%"
                ),
                rx.link(
                    rx.button(
                        rx.icon(
                            "user-pen"
                            ), 
                        "Personal", 
                        width="100%", 
                        height="40px", 
                        variant="ghost", 
                        radius="none", 
                        justify_content="start", 
                        color="white"
                    ),
                    href="/personal",
                    width="100%"
                ),
                rx.link(
                    rx.button(
                        rx.icon(
                            "form"
                            ),
                        "Formularios", 
                        width="100%", 
                        height="40px", 
                        variant="ghost", 
                        radius="none", 
                        justify_content="start", 
                        color="white"
                    ),
                    href="/formularios",
                    width="100%",
                ),
                rx.link(
                    rx.button(
                        rx.icon(
                            "file-text"
                            ), 
                        "Documentos", 
                        width="100%", 
                        height="40px",
                        variant="ghost", 
                        radius="none", 
                        justify_content="start", 
                        color="white"
                    ),
                    href="/documentos",
                    width="100%"
                ),
                rx.link(
                    rx.button(
                        rx.icon(
                            "proportions"
                            ),
                        "Reportes", 
                        width="100%", 
                        height="40px",
                        variant="ghost", 
                        radius="none", 
                        justify_content="start", 
                        color="white"
                    ),
                    href="/reportes",
                    width="100%",
                ),
                rx.button(
                    rx.icon(
                        "X"
                        ),
                    "Salir", 
                    width="100%", 
                    height="40px", 
                    variant="ghost", 
                    radius="none", 
                    justify_content="start", 
                    color="white"
                ),
            width="15%",
            min_height="90vh",
            bg="#064e3b",
            spacing="3",
            padding_left="10px",
            ),