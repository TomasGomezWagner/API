from fastapi import APIRouter

prueba_router = APIRouter(prefix='/prueba', tags=['prueba'])


@prueba_router.get('/')
async def prueba():
    return {'hola':'mundo'}