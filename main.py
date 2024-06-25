from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.events import event_router
from routes.users import user_route
from database.connections import conn
import uvicorn


app = FastAPI()
app.include_router(user_route, prefix='/users')
app.include_router(event_router, prefix='/events')


@app.on_event("startup")
def on_startup():
    conn()


@app.get('/')
async def home():
    return RedirectResponse(url="/event/")


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)




