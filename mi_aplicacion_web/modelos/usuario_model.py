import reflex as rx
from typing import Optional
from sqlmodel import Field

class USUARIOS_TBL(rx.Model, table=True):
    id_usuario: int = Field(default=None, primary_key=True)
    nombre: str 
    apellido: str
    user_alias: str
    contrasena_hash: str
    email: str