from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from routes.events import event_router
from routes.products import product_router
from routes.users import user_route
from database.connections import Settings
import uvicorn

#Register the origins
origins = ["*"]

settings = Settings()

app = FastAPI(title='Event Api')
app.include_router(user_route, prefix='/users')
app.include_router(event_router, prefix='/events')
app.include_router(product_router, prefix="/products")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.on_event("startup")
async def init_db():
    await settings.initialize_database()


@app.get('/')
async def home():
    return RedirectResponse(url="/event/")


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)
