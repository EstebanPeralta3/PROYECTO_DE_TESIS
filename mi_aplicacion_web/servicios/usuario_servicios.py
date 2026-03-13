from ..repositorios.usuario_repositorio import (select_from_usuarios_repo,
                                                insert_into_repo,
                                                select_from_usuarios_where_repo,
                                                borrar_usuario_repo,
                                                editar_usuario_repo)
from ..modelos.usuario_model import USUARIOS_TBL

# Servicio que muestra todos los registros de la tabla usuarios
def select_from_usuarios_serv():
    usuarios = select_from_usuarios_repo()
    print(usuarios)
    return usuarios

# Servicio que muestra el usuario si es que existe el alias dado un parametro
def select_from_usuarios_where_serv(alias_ser: str):
    if (len(alias_ser) != 0):
        select_from_usuarios_where_repo(alias_ser)
    else:
        select_from_usuarios_repo()

# Servicio que permite crear un usuario
def insert_into_serv(nombre: str,
                     apellido: str,
                     contrasena_hash: str,
                     user_alias: str,
                     email: str):
    usuario_existe = select_from_usuarios_where_repo(user_alias)

    if (len(usuario_existe) == 0):
        usuario_a_insertar = USUARIOS_TBL(nombre=nombre,
                                          apellido=apellido,
                                          contrasena_hash=contrasena_hash,
                                          user_alias=user_alias,
                                          email=email)
        return insert_into_repo(usuario_a_insertar)
    else:
        print("El usuario ya existe")
        raise BaseException("El usuario ya existe")
    
# Eliminar un usuario
def borrar_usuario_serv(useralias_serv: str):
    return borrar_usuario_repo(useralias_repo=useralias_serv)
    
# Editar los datos de un usuario
def editar_usuario_serv(edit_useralias_serv: str, edit_datos_serv: dict):
    if edit_datos_serv["nombre"] == "":
        raise BaseException("El campo nombre no puede estar vacío.")
    if edit_datos_serv["apellido"] == "":
        raise BaseException("El campo apellido no puede estar vacío.")
    if edit_datos_serv["contrasena_hash"] == "":
        raise BaseException("El campo contraseña no puede estar vacío.")
    if edit_datos_serv["user_alias"] == "":
        raise BaseException("El campo alias no puede estar vacío.")
    if edit_datos_serv["email"] == "":
        raise BaseException("El campo email no puede estar vacío.")
    
    return editar_usuario_repo(edit_useralias_serv, edit_datos_serv)