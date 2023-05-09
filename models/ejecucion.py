from config.databse import Base
from sqlalchemy import Column, String, Integer

class Ejecucion(Base):

    __tablename__ = 'ejecucion'

    id          = Column(Integer, primary_key=True)
    prioridad   = Column(String)
    parar       = Column(Integer)