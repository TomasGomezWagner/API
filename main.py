from fastapi import FastAPI

from config.databse import engine, Base

from middlewares.error_handler import ErrorHandler
from middlewares.set_json_response import JSONMiddleware

from routers.protocolo import protocolo_router
from routers.ejecucion import ejecucion_router
from routers.prueba import prueba_router

app = FastAPI()
app.title = 'Api para Desencriptador'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.add_middleware(JSONMiddleware)
app.include_router(protocolo_router)
app.include_router(ejecucion_router)

app.include_router(prueba_router)

Base.metadata.create_all(bind=engine)



