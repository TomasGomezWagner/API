from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Union

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.databse import Session

from models.ejecucion import Ejecucion as EjecucionModel
from services.ejecucion import EjecucionService

ejecucion_router = APIRouter(prefix='/ejecucion', tags=['ejecucion'])


class Ejecucion(BaseModel):
    id:         Optional[int]
    prioridad:  Optional[str]
    parar:      bool

    class Config:
        schema_extra = {
            'example':{
                'id':1,
                'prioridad' : 'NEO',
                'parar' : 0,
            }
        }


@ejecucion_router.post('/')
async def agregar_ejecucion(item:Ejecucion):
    db = Session()
    result = EjecucionService(db).agregar_ejecucion(item)
    return JSONResponse(status_code=201, content={'message':f'Se actualizo la ejecucion {result.prioridad=}, {result.parar=}'})


@ejecucion_router.get('/')
async def ultimo_criterio_ejecucion():
    db = Session()
    result = EjecucionService(db).buscar_ultimo()
    return JSONResponse(status_code=201, content=jsonable_encoder(result))