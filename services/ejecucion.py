from models.ejecucion import Ejecucion as EjecucionModel


class EjecucionService:

    def __init__(self, db) -> None:
        self.db = db


    def agregar_ejecucion(self, item):
        new_item = EjecucionModel(**item.dict())
        del new_item.id
        self.db.add(new_item)
        self.db.commit()
        return new_item
    
    def buscar_ultimo(self,):
        result = self.db.query(EjecucionModel).order_by(EjecucionModel.id.desc()).first()
        return result