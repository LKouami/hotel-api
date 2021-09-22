from fastapi import FastAPI
from butler.models import models
from butler.database import database
from butler.routers import blog, user, authentication

app = FastAPI()
 
models.database.Base.metadata.create_all(database.engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)




