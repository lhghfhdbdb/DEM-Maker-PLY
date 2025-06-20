from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import drone, websockets, ply_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://tauri.localhost"],
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=[
        "Content-Type",
        "Accept",
        "Origin",
    ],
)
app.include_router(drone.router)
app.include_router(websockets.router)
app.include_router(ply_router.router)  # 注册 ply_router
