from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
        
class JSONMiddleware(BaseHTTPMiddleware):
    
    async def dispatch(self, request: Request, call_next) -> JSONResponse:
        response = await call_next(request)
        response.headers["Content-Type"] = "application/json"
        return response
    