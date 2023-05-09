from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.databse import Session
from models.protocolo import Protocolo as ProtocoloModel
from services.protocolo import ProtocoloService


protocolo_router = APIRouter(prefix='/protocolo', tags=['protocolo'])


class Protocolo(BaseModel):
    id: Optional[int]
    protocolo: int
    estado : int

    class Config:
        schema_extra = {
            'example':{
                'id': 1,
                'protocolo': 123456,
                'estado': 0,
            }
        }


@protocolo_router.post('/')
async def agregar_protocolo(protocolo:Protocolo):
    db = Session()
    result = ProtocoloService(db).agregar_protocolo(protocolo)
    return JSONResponse(status_code=201, content={'message':f'Se agrego el protocolo {result.id}'})


@protocolo_router.get('/ultimo')
async def buscar_ultimo():
    db = Session()
    result = ProtocoloService(db).buscar_ultimo()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@protocolo_router.get('/all')
async def buscar_all() -> list[Protocolo]:
    db = Session()
    result = db.query(ProtocoloModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@protocolo_router.get('/{id}', response_model=Protocolo)
async def buscar_path( id:int ) -> Protocolo:
    return buscar(id)


@protocolo_router.get('/')
async def buscar_por_query(id:int):
    return buscar(id)


def buscar(id:int):
    db = Session()
    result = ProtocoloService(db).buscar_protocolo(id)
    if not result:
        return JSONResponse(status_code=404, content={'message':'El protocolo no existe'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



#----------------------- ejemplo sin funcion extra ---------------------------

# @protocolo_router.get('/{id}', response_model=Protocolo)
# async def buscar_path( id:int) -> Protocolo:
#     db = Session()
#     result = ProtocoloService(db).buscar_protocolo(id)
#     if not result:
#         return JSONResponse(status_code=404, content={'message':'El protocolo no existe'})
#     return JSONResponse(status_code=200, content=jsonable_encoder(result))


# @protocolo_router.post('/agregar-protocolo', response_model=dict, status_code=201)
# async def agregar_protocolo(item:Protocolo):
#     db = Session()
#     new_protocolo = ProtocoloModel(**item.dict())
#     db.add(new_protocolo)
#     db.commit()
#     return JSONResponse(status_code=201, content={'message':f'Se agrego el protocolo {item.protocolo}'})