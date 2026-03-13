import reflex as rx
from .estructura_de_menu import encabezado, menu_lateral
from .modelos.usuario_model import USUARIOS_TBL
from .servicios.usuario_servicios import (select_from_usuarios_serv,
                                          insert_into_serv,
                                          select_from_usuarios_where_serv,
                                          borrar_usuario_serv,
                                          editar_usuario_serv
                                          )
from mi_aplicacion_web.notificacion import notificacion_de_error
import asyncio
from .estilos.estilo_tabla import (style_table,
                                   style_header,
                                   style_row)

class UsuarioState(rx.State):

    # variable de tipo usuarios_tbl
    usuarios: list[USUARIOS_TBL]

    # variable donde se guardan los errores
    mensaje_error: str

    # valor por cual buscar
    filtrar_por: str

    # cambia el valor de la variable de estado por el que se ingresa en pantalla
    @rx.event
    def buscar(self, valor: str):
        self.filtrar_por = valor
    
    # Devuelve todos los registros de la tabla usuarios
    # Llama al servicio select_from_usuarios_serv
    async def select_from_usuarios(self):
        async with self:
            self.usuarios = select_from_usuarios_serv()

    # Inserta un registro, llamando primero al servicio insert_into_serv
    # Si hay algun tipo de error, manda mensaje
    async def insert_into(self, dato: dict):
        try:
            async with self:
                self.usuarios = insert_into_serv(nombre = dato["nombre"],
                                                 apellido = dato["apellido"],
                                                 contrasena_hash = dato["contrasena_hash"],
                                                 user_alias = dato["user_alias"],
                                                 email = dato["email"],)
        except BaseException as be:
            print(be.args)
            self.mensaje_error = be.args[0]
        self.usuarios = select_from_usuarios_serv()

    # Función de estado, borrar usuario
    async def borrar_usuario(self, useralias: str):
        async with self:
            self.usuarios = borrar_usuario_serv(useralias)

    # Función de estado, editar un usuario
    async def editar_usuario(self, datos_form: dict):
        try:
            async with self:
                editar_usuario_serv(edit_useralias_serv=datos_form["alias_oculto"],
                                    edit_datos_serv=datos_form)
        except BaseException as be:
            print(be.args)
            self.mensaje_error = be.args[0]
        self.usuarios = select_from_usuarios_serv()


# Dialog para asignar un rol al usuario
def asignar_rol_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("shield-user", color="white", size=15),
                color_scheme="purple",
                size="1",
                radius="full"
            )
        ),
        rx.dialog.content(
            rx.dialog.title("Asignar roles", color= "#064e3b"),
            rx.dialog.description("Seleccione un rol del listado."),
            rx.vstack(
                rx.separator(),
                rx.spacer(),
                rx.select(
                    ["Administrador", "Usuario Básico"],
                    placeholder="Seleccione",
                    default_value="Seleccione",
                    radius="full",
                    variant="soft"
                ),
                rx.separator(),
                rx.spacer(),
                rx.dialog.close(
                    rx.button("Guardar", color_scheme="blue", variant="solid")
                ),
                align_items="center"
            ),
            style={"width":"300px"}
        )
    )
# Formulario de editar un usuario
def editar_usuario_form(usuario_form: USUARIOS_TBL) -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.separator(),
            rx.input(
                type="hidden",
                name="alias_oculto",
                default_value=usuario_form.user_alias,
                display="none"
            ),
            rx.hstack(
                rx.text("Nombre:", width="120px"),
                rx.input(
                    name="nombre",
                    default_value=usuario_form.nombre,
                    variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.hstack(
                rx.text("Apellido:", width="120px"),
                rx.input(
                    name="apellido",
                    default_value=usuario_form.apellido,
                    variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.hstack(
                rx.text("Contraseña:", width="120px"),
                rx.input(
                    name="contrasena_hash",
                    type="password",
                    default_value=usuario_form.contrasena_hash,
                    variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.hstack(
                rx.text("Alias:", width="120px"),
                rx.input(
                    name="user_alias",
                    default_value=usuario_form.user_alias,
                    variant="soft"
                ),
                width="100%",
                align_items="center"
            ),
            rx.hstack(
                rx.text("Email:", width="120px"),
                rx.input(
                    name="email",
                    default_value=usuario_form.email,
                    variant="soft"
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
            )
        ),
        on_submit= lambda form: UsuarioState.editar_usuario(form)
    )

# Dialog para editar un usuario
def editar_usuario_dialog(usuario_dialog: USUARIOS_TBL) -> rx.Component:
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
            rx.dialog.title(
                "Editar usuario", color= "#064e3b"
            ),
            rx.dialog.description(
                "Modifique los campos que desea editar."
            ),
            editar_usuario_form(usuario_dialog),
            style={"width":"350px"}
        ),
    )

# Formulario para crear usuario
def crear_usuario_form() -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.input(
                placeholder="Nombre", name="nombre"
            ),
            rx.input(
                placeholder="Apellido", name="apellido"
            ),
            rx.input(
                placeholder="Contraseña", name="contrasena_hash", type="password"
            ),
            rx.input(
                placeholder="Alias", name="user_alias"
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
            align="center"
        ),
        on_submit=UsuarioState.insert_into()
    )

# Dialog para borrar usuario
def borrar_usuario_dialog(useralias_dialog: str, nombre_dialog: str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.icon("trash-2", color="white", size=15),
                radius="full",
                size="1",
                style={"bg":"#dc3545"}
            )
        ),
        rx.dialog.content(
            rx.dialog.title(
                "Borrar Usuario", color="#064e3b"
            ),
            rx.dialog.description(
                f"¿Quiéres eliminar a {nombre_dialog}?. La acción es permanente."
            ),
            rx.hstack(
                rx.dialog.close(
                    rx.button("Cancelar", color_scheme="gray", variant="soft")
                ),
                rx.dialog.close(
                    rx.button("Eliminar", color_scheme="red", variant="solid",
                              on_click=UsuarioState.borrar_usuario(useralias_dialog))
                ),
                sacing="3",
                margin_top="16px",
                justify="end"
            ),
            width="100%"
        )
    )

# Dialog para crear usuario
def crear_usuario_dialog() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.hstack(
                rx.icon("plus"),
                rx.text("Nuevo registro"),
                spacing="1"
                ),
                variant="ghost"
            )
        ),
        rx.dialog.content(
            rx.vstack(
                rx.dialog.title("Crear usuario", align="center", color= "#064e3b"),
                rx.dialog.description("Complete el formulario para crear un nuevo usuario", align="center"),
                crear_usuario_form(),
                spacing="3",
                align="center"
            ),
            style={"width":"300px"},
        )
    )

# Creamos el encabezado de la tabla
def tabla_usuarios(lista_usuarios: list[USUARIOS_TBL]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.row_header_cell("Nombre"),
                rx.table.row_header_cell("Apellido"),
                rx.table.row_header_cell("Alias"),
                rx.table.row_header_cell("Email"),
                rx.table.row_header_cell("Rol"),
                rx.table.row_header_cell(""),
                color="white"
            ),
            style=style_header
        ),
        rx.table.body(
            rx.foreach(lista_usuarios, tabla_usuarios_body)
        ),
        style=style_table
    )

# Creamos las filas de la tabla usuarios
def tabla_usuarios_body(usuario: USUARIOS_TBL) -> rx.Component:
    return rx.table.row(
        rx.table.cell(usuario.nombre),
        rx.table.cell(usuario.apellido),
        rx.table.cell(usuario.user_alias),
        rx.table.cell(usuario.email),
        rx.table.cell(
            rx.badge(
                "Asignar rol",
                color_scheme="blue"
            )
        ),
        rx.table.cell(
            rx.hstack(
                asignar_rol_dialog(),
                editar_usuario_dialog(usuario),
                borrar_usuario_dialog(usuario.user_alias, usuario.nombre)
                ,
                spacing="3"
            )
        ),
        style=style_row
    )

# Iteracion busqueda, agregar
def interacion():
    return rx.hstack(
        rx.hstack(
            rx.input(placeholder="Alias",
                    on_change=UsuarioState.buscar),
            rx.button(
                rx.icon("search"),
                color_scheme="grass",
                variant="ghost",
                on_click=UsuarioState.select_from_usuarios
            ),
            padding_right="60px"
        ),
        crear_usuario_dialog(),
    )

def contenido() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Administración", align="center", color= "#064e3b"),
            interacion(),
            tabla_usuarios(UsuarioState.usuarios),
            spacing="3",
            align_items="center",
            margin_top="10px"
        ),
        width="100%",
        padding="6",
    )

# Ruta /administracion 
# Titulo Administracion 
# Al cargar la pagina llama a la función select_from_usuarios
@rx.page(route="/administracion",
         title="Administración",
         on_load=UsuarioState.select_from_usuarios)
def administracion() -> rx.Component:
    return rx.vstack(
        encabezado(),
        rx.hstack(
            menu_lateral(),
            contenido(),
            width="100%",
        ),
        spacing="0"
    )