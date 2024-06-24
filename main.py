from fastapi import FastAPI

from routes.events import event_router
from routes.users import user_route
import uvicorn


app = FastAPI()
app.include_router(user_route, prefix='/users')
app.include_router(event_router, prefix='/events')

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)




