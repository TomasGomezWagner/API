from fastapi import FastAPI

from config.databse import engine, Base

from middlewares.error_handler import ErrorHandler

from routers.protocolo import protocolo_router
from routers.ejecucion import ejecucion_router

app = FastAPI()
app.title = 'Api para Desencriptador'
app.version = '0.0.1'

app.add_middleware(ErrorHandler)
app.include_router(protocolo_router)
app.include_router(ejecucion_router)

Base.metadata.create_all(bind=engine)



