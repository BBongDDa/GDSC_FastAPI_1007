from fastapi import FastAPI


from GDSC import models
from GDSC.database import engine
from GDSC.routers import user_ro

app = FastAPI()

@app.get('/')
def hello():
    return "Hello, GDSC!"

# Router Setting
app.include_router(user_ro.router)

# DB Setting
models.Base.metadata.create_all(engine)
