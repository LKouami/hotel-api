from sqlalchemy.sql.functions import user
from fastapi import FastAPI
from app.butler.models import models
from app.butler.database import database
from app.butler.routers import blog, user, authentication

app = FastAPI()
 
models.database.Base.metadata.create_all(database.engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)




