from config.databse import Base
from sqlalchemy import Column, Integer

class Protocolo(Base):

    __tablename__ = 'protocolos'

    id          = Column(Integer, primary_key=True)
    protocolo   = Column(Integer)
    estado      = Column(Integer)
