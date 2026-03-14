#from sqlmodel import create_engine
from sqlalchemy import create_engine

def connect():
    engine = create_engine("oracle+oracledb://jbz_docs:1234@192.168.245.1:1521/?service_name=XEPDB1")
    return engine

