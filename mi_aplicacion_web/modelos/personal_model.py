import reflex as rx
from typing import Optional
from sqlmodel import Field

class PERSONAL_TBL(rx.Model, table=True):
    id_personal: int = Field(default=None, primary_key=True)
    cedula_per: str 
    nombre_per: str 
    apellido_per: str 
    area_per: str
    cargo_per: str
    email: str 
    id_usuario: str