import reflex as rx
from .estructura_de_menu import encabezado, menu_lateral
from .modelos.personal_model import PERSONAL_TBL
from .servicios.personal_servicios import (seleccionar_todo_el_personal_sevicio,
                                           seleccionar_person_por_email_servicio,
                                           crear_personal_servivio,
                                           borrar_pesonal_servicio,
                                           actualizar_personal_serv)
from mi_aplicacion_web.notificacion import notificacion_de_error
import asyncio
from .estilos.estilo_tabla import (style_table,
                                   style_header,
                                   style_row)

class PersonalState(rx.State):
     
     # variable con una lista de tipo PERSONAL_TBL
    personales: list[PERSONAL_TBL]
     
     # variable con el dato que se quiere filtrar
    filtrar_por: str

     # variable que contiene el mensaje de error
    mensaje_error: str = ""

    # Varible para guardar datos de la persona a actualizar
    person_act: dict

    @rx.event
    def guardar_seleccion(self, valor: dict):
        self.person_act = valor

    async def establecer_todo_el_personal(self):
        async with self:
            self.personales = seleccionar_todo_el_personal_sevicio()

    async def establecer_person_por_email(self):
        async with self:
            self.personales = seleccionar_person_por_email_servicio(self.filtrar_por)

    async def borrar_person_por_cedula(self, ced: str):
        async with self:
            self.personales = borrar_pesonal_servicio(ced)

    async def crear_personal(self, datos: dict):
        try:
            async with self:
                self.personales = crear_personal_servivio(cedula=datos["cedula"], 
                                                          nombre=datos["nombre"],
                                                          apellido=datos["apellido"],
                                                          area=datos["area"],
                                                          cargo=datos["cargo"],
                                                          email=datos["email"])
        except BaseException as be:
            print(be.args)
            self.mensaje_error = be.args[0]
            yield
        await self.duracion_error()
        self.personales = seleccionar_todo_el_personal_sevicio()

    rx.event()
    def buscar_on_change(self, valor: str):
        self.filtrar_por = valor

    async def duracion_error(self):
        async with self:
            await asyncio.sleep(2)
            self.mensaje_error = ""

    async def actualizar_personal(self, dato_form: dict):
        try:
            async with self:
                actualizar_personal_serv(ced=dato_form["cedula_oculta"], datos=dato_form)
        except BaseException as be:
            print(be.args)
            self.mensaje_error = be.args[0]
            yield
        await self.duracion_error()
        self.personales = seleccionar_todo_el_personal_sevicio()


# Form de actualización
def form_actualizacion(person_form: PERSONAL_TBL) -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.separator(),
            rx.spacer(),
            rx.input(
                type="hidden",
                name="cedula_oculta",
                value=person_form["cedula_per"],
                display="none"
            ),
            rx.hstack(
                rx.text("Cédula:", width="120px"),
                rx.input(
                    default_value=person_form["cedula_per"], name="cedula", variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.hstack(
                rx.text("Nombre:", width="120px"),
                rx.input(
                    default_value=person_form["nombre_per"], name="nombre", variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.hstack(
                rx.text("Apellido:", width="120px"),
                rx.input(
                    default_value=person_form["apellido_per"], name="apellido", variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.hstack(
                rx.text("Area:", width="120px"),
                rx.input(
                    default_value=person_form["area_per"], name="area", variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.hstack(
                rx.text("Cargo:", width="120px"),
                rx.input(
                    default_value=person_form["cargo_per"], name="cargo", variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.hstack(
                rx.text("Email:", width="120px"),
                rx.input(
                    default_value=person_form["email"], name="email", variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.spacer(),
            rx.separator(),
            rx.hstack(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button("Guardar", color_scheme="blue", variant="solid", type="submit")
                ),
                spacing="1",
                margin_top="10px",
                margin_left="140px"
            ),
        ),
        on_submit=lambda datos: PersonalState.actualizar_personal(
            datos
        )
    )

# Dialog de actualizar
def actualizar_dialog(person: PERSONAL_TBL)-> rx.Component:
    return rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    rx.icon("pencil", size=15),
                    bg="#fdb436",
                    size="1",
                    radius="full"
                )
            ),
            rx.dialog.content(
                rx.dialog.title("Actualizar Personal", color= "#064e3b"),
                rx.dialog.description(
                    "Modifique los campos que desea editar."
                ),
                form_actualizacion(person),
                style={"width":"350px"}
            )
        )

 # Creamos la tabla con sus encabezados
def tabla_personal(lista_personal: list[PERSONAL_TBL]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Cedula"),
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Apellido"),
                rx.table.column_header_cell("Area"),
                rx.table.column_header_cell("Cargo"),
                rx.table.column_header_cell("Email"),
                rx.table.column_header_cell(""),
                color="white"
            ),
            style=style_header
        ),
        rx.table.body(
            rx.foreach(lista_personal, tabla_fila)
        ),
        style=style_table
    )

 # mostramos los datos que van en el cuerpo de la tabla
def tabla_fila(per: PERSONAL_TBL) -> rx.Component:
    return rx.table.row(
        rx.table.cell(per.cedula_per),
        rx.table.cell(per.nombre_per),
        rx.table.cell(per.apellido_per),
        rx.table.cell(per.area_per),
        rx.table.cell(per.cargo_per),
        rx.table.cell(per.email),
        rx.table.cell(
            rx.hstack(
                actualizar_dialog(per),
                borrar_person_dialog(per.cedula_per, per.nombre_per),
                spacing="3"
            )
        ),
        style=style_row
    )

 # Creamos un formulario para el dialog
def crear_person_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Cédula", name="cedula"
            ),
            rx.input(
                placeholder="Nombre", name="nombre"
            ),
            rx.input(
                placeholder="Apellido", name="apellido"
            ),
            rx.input(
                placeholder="Área", name="area"
            ),
            rx.input(
                placeholder="Cargo", name="cargo"
            ),
            rx.input(
                placeholder="Email", name="email"
            ),
            rx.hstack(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button("Guardar", color_scheme="blue", variant="solid", type="submit")
                ),
                spacing="9",
                margin_top="10px"
            ),
        ),
        on_submit=PersonalState.crear_personal
    )

 # Creamos el componente dialog
def crear_person_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.hstack(rx.icon("plus"), rx.text("Nuevo registro"), spacing="1"), variant="ghost")
        ),
        rx.dialog.content(
            rx.vstack(
                rx.dialog.title("Nuevo registro"),
                rx.dialog.description("Complete los campos para crear un nuevo registro.", size="2", margin_bottom="16px"),
                crear_person_form(),
                spacing="3",
                align="center"
            ),
            style={"width":"300px"}
        )
    )

 # Creamos el componente dialog de borrado
def borrar_person_dialog(ced: str, nombre: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(rx.icon("trash-2", size=15), bg="#dc3545", size="1", radius="full")
        ),
        rx.dialog.content(
            rx.dialog.title("Eliminar personal"),
            rx.dialog.description(f"¿Estás seguro de querer eliminar a {nombre}?. La acción es permanente."),
            rx.hstack(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button("Eliminar", color_scheme="red", variant="solid", on_click=PersonalState.borrar_person_por_cedula(ced))
                ),
                sacing="3",
                margin_top="16px",
                justify="end"
            ),
            width="100%"
        )
    )

def iteracion() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.input(
                placeholder="Ingrese email",
                on_change= PersonalState.buscar_on_change
            ),
            rx.button(
                rx.icon("search"),
                color_scheme="grass",
                variant="ghost",
                on_click=PersonalState.establecer_person_por_email
            ),
            padding_right="60px"
        ), 
        crear_person_dialog()
    )

def contenido() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Personal", align="center", color="#064e3b"),
            iteracion(),
            tabla_personal(PersonalState.personales),
            spacing="3",
            align="center",
            margin_top="10px"
        ),
        rx.cond(
            PersonalState.mensaje_error != "",
            notificacion_de_error(PersonalState.mensaje_error, "alert", "yellow"),
        ),
        padding="6",
        width="100%",
    )

@rx.page(route="/personal", 
        title="Personal",
        on_load=PersonalState.establecer_todo_el_personal,)
def personal() -> rx.Component:
    return rx.vstack(
        encabezado(),
        rx.hstack(
            menu_lateral(),
            contenido(),
            width="100%"
        ),
        spacing="0",
    )