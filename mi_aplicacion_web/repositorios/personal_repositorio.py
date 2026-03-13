from ..modelos.personal_model import PERSONAL_TBL
from .connect_db import connect
from sqlmodel import Session, select

# Muestra todos los registros de la tabla, 
# SELECT * FROM personal_tbl
def seleccionar_todos():
    engine = connect()
    with Session(engine) as session:
        query = select(PERSONAL_TBL)
        return session.exec(query).all()

 # select * from PERSONAL_TBL where nombre_per = email
def seleccionar_person_por_email(email: str):
    engine = connect()
    with Session(engine) as session:
        query = select(PERSONAL_TBL).where(PERSONAL_TBL.email == email)
        return session.exec(query).all()
 
# Metodo para crear un personal, recibe un parametro de tipo PERSONAL_TBL
# es un INSERT INTO personal_tbl VALUES()

def crear_personal(person: PERSONAL_TBL):
    engine = connect()
    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)
        query=select(PERSONAL_TBL)
        return session.exec(query).all()
    
# Metodo que permite eliminar un registro 
def borrar_pesonal(cedula: str):
    engine = connect()
    with Session(engine) as session:
        query = select(PERSONAL_TBL).where(PERSONAL_TBL.cedula_per == cedula)
        usuario_a_borrar = session.exec(query).one()
        session.delete(usuario_a_borrar)
        session.commit()
        query = select(PERSONAL_TBL)
        return session.exec(query).all()
    
# Metodo que actualiza el personal seleccionado
def actualizar_personal_repo(cedula: str, datos: dict):
    engine = connect()
    with Session(engine) as session:
        query = select(PERSONAL_TBL).where(PERSONAL_TBL.cedula_per == cedula)
        usuario_actualizar = session.exec(query).first()
        
        if usuario_actualizar is None:
            raise BaseException("Registro no encontrado")
        
        usuario_actualizar.cedula_per = datos["cedula"]
        usuario_actualizar.nombre_per = datos["nombre"]
        usuario_actualizar.apellido_per = datos["apellido"]
        usuario_actualizar.area_per = datos["area"]
        usuario_actualizar.cargo_per = datos["cargo"]
        usuario_actualizar.email = datos["email"]
        session.add(usuario_actualizar)
        session.commit()
        session.refresh(usuario_actualizar)

        return usuario_actualizar

    

    