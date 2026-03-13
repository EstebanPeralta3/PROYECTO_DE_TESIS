from ..repositorios.personal_repositorio import (seleccionar_todos,
                                                seleccionar_person_por_email, 
                                                crear_personal, borrar_pesonal, 
                                                actualizar_personal_repo
                                            )
from ..modelos.personal_model import PERSONAL_TBL

 # Funcion que devuelve todo el personal seleccionado, 
 # SELECT * FROM personal_tbl
def seleccionar_todo_el_personal_sevicio():
    personales = seleccionar_todos()
    print(personales)
    return personales

 # Funcion que devuelve todos los datos del personal, filtrado por email, 
 # SELECT * FROM personal_tbl WHERE email = parametro
def seleccionar_person_por_email_servicio(email: str):
    if (len(email) != 0):
        return seleccionar_person_por_email(email)
    else:
        return seleccionar_todos()


 # Funcion que permite crear o cargar un personal a la BD
 # Con algunas validaciones
def crear_personal_servivio(cedula: str, 
                            nombre: str, 
                            apellido: str, 
                            area: str, 
                            cargo: str, 
                            email: str):
    person = seleccionar_person_por_email(email)
    
    if (len(person) == 0):
        guardar_person = PERSONAL_TBL(cedula_per=cedula, 
                                      nombre_per=nombre, 
                                      apellido_per=apellido, 
                                      area_per=area, 
                                      cargo_per=cargo, 
                                      email=email)
        return crear_personal(guardar_person)
    else:
        print("El usuario ya existe")
        raise BaseException("El usuario ya existe")
    
 # Funcion que permite eliminar un personal
def borrar_pesonal_servicio(cedula: str):
    return borrar_pesonal(cedula=cedula)

# Función que muestra los datos de un registro para editarlo
def actualizar_personal_serv(ced: str, datos: dict):
    if datos["cedula"] == "":
        raise BaseException("La cédula no puede estar vacia")
    if datos["nombre"] == "":
        raise BaseException("El nombre no puede estar vacio")
    if datos["apellido"] == "":
        raise BaseException("El apellido no puede estar vacio")
    if datos["email"] == "":
        raise BaseException("El email no puede estar vacio")
    
    return actualizar_personal_repo(ced, datos)
