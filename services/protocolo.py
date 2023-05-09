from models.protocolo import Protocolo as ProtocoloModel


class ProtocoloService:
    
    def __init__(self, db) -> None:
        self.db = db
        

    def buscar_protocolo(self, id):
        result = self.db.query(ProtocoloModel).filter(ProtocoloModel.id == id).first()
        return result


    def buscar_ultimo(self):
        result = self.db.query(ProtocoloModel).order_by(ProtocoloModel.id.desc()).first()
        return result
    

    def agregar_protocolo(self, protocolo):
        new_protocolo = ProtocoloModel(**protocolo.dict())
        del new_protocolo.id
        self.db.add(new_protocolo)
        self.db.commit()
        return new_protocolo

