from ..modelos.usuario_model import USUARIOS_TBL
from .connect_db import connect
from sqlmodel import Session, select

# Muestra todos los registros de la tabla usuarios_tbl,
# SELECT * FROM usuarios_tbl
def select_from_usuarios_repo():
    engine = connect()
    with Session(engine) as session:
        query = select(USUARIOS_TBL)
        return session.exec(query).all()
    
# Añade un nuevo usuario a la tabla usuarios_tbl
# INSERT INTO usuarios_tbl, recibiendo un parametro de tipo USUARIOS_TBL
def insert_into_repo(usuario: USUARIOS_TBL):
    engine = connect()
    with Session(engine) as session:
        session.add(usuario)
        session.commit()
        session.refresh(usuario)
        query = select(USUARIOS_TBL)
        return session.exec(query).all()

# Selecciona un usuario por su alias
def select_from_usuarios_where_repo(alias: str):
    engine = connect()
    with Session(engine) as session:
        query = select(USUARIOS_TBL).where(USUARIOS_TBL.user_alias == alias)
        return session.exec(query).all()
    
# Eliminar un usuario
def borrar_usuario_repo(useralias_repo: str):
    engine = connect()
    with Session(engine) as session:
        query = select(USUARIOS_TBL).where(USUARIOS_TBL.user_alias == useralias_repo)
        usuario_a_borrar = session.exec(query).one()
        session.delete(usuario_a_borrar)
        session.commit()
        query = select(USUARIOS_TBL)
        return session.exec(query).all()
    
# Editar información de un usuario
def editar_usuario_repo(edit_userlias_repo: str, edit_datos_repo: dict):
    engine = connect()
    with Session(engine) as session:
        query = select(USUARIOS_TBL).where(USUARIOS_TBL.user_alias == edit_userlias_repo)
        usuario_a_editar = session.exec(query).one()

        if usuario_a_editar is None:
            raise BaseException("Registro no encontrado")
        
        usuario_a_editar.nombre = edit_datos_repo["nombre"]
        usuario_a_editar.apellido = edit_datos_repo["apellido"]
        usuario_a_editar.contrasena_hash = edit_datos_repo["contrasena_hash"]
        usuario_a_editar.user_alias = edit_datos_repo["user_alias"]
        usuario_a_editar.email = edit_datos_repo["email"]

        session.add(usuario_a_editar)
        session.commit()
        session.refresh(usuario_a_editar)

        return usuario_a_editar
    
# Repositorio para asignar roles

        